import os
import logging
from neo4j import GraphDatabase
from retry import retry
import pandas as pd
import numpy as np

from neo4j_csv_importer.config import NEO4J_DATABASE

LOGGER = logging.getLogger(__name__)


class Neo4jLoader:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def _set_uniqueness_constraints(self, tx, node):
        query = f"CREATE CONSTRAINT IF NOT EXISTS FOR (n:{node}) REQUIRE n.id IS UNIQUE;"
        tx.run(query)

    def set_constraints(self, nodes):
        with self.driver.session(database=NEO4J_DATABASE) as session:
            for node in nodes:
                session.write_transaction(self._set_uniqueness_constraints, node)

    def _prepare_query_and_params(self, node_type, row):
        non_null_properties = {key: value for key, value in row.items() if value is not None}
        properties = ', '.join([f"{key}: ${key}" for key in non_null_properties.keys()])
        query = f"MERGE (n:{node_type} {{{properties}}})"
        return query, non_null_properties

    @retry(tries=100, delay=10)
    def load_nodes(self, csv_handler, filenames):
        for filename in filenames:
            node_type = os.path.splitext(filename)[0]
            LOGGER.info(f"Loading {node_type} nodes")
            df = csv_handler.read_csv(filename)
            with self.driver.session(database=NEO4J_DATABASE) as session:
                for _, row in df.iterrows():

                    row_dict = row.to_dict()
                    # Convert NaN values to None
                    for key, value in row_dict.items():
                        if pd.isna(value):
                            row_dict[key] = None

                    query, params = self._prepare_query_and_params(node_type, row_dict)
                    try:
                        session.run(query, params)
                    except Exception as e:
                        LOGGER.warning(f"Error while loading {node_type} node with data {params}: {e}")

    @retry(tries=100, delay=10)
    def load_relationships(self, relationship_configs):
        with self.driver.session(database=NEO4J_DATABASE) as session:
            self._load_relationships(session, relationship_configs)

    def _load_relationships(self, session, relationship_configs):
        for config in relationship_configs:
            LOGGER.info(f"Loading {config['type']} relationships")
            try:
                session.run(config['query'])
            except Exception as e:
                LOGGER.warning(f"Error while loading {config['type']} relationships: {e}")
