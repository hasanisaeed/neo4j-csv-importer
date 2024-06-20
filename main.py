import os
import json
import logging
from neo4j_csv_importer.config import CSV_DIR, NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD
from neo4j_csv_importer.neo4j_loader import Neo4jLoader
from neo4j_csv_importer.csv_handler import CSVHandler
from neo4j_csv_importer.utils import get_csv_files

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

LOGGER = logging.getLogger(__name__)


def load_relationship_configs(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)["relationships"]


def main():
    csv_handler = CSVHandler(CSV_DIR)
    neo4j_loader = Neo4jLoader(NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD)

    try:
        LOGGER.info("Getting list of CSV files")
        csv_files = get_csv_files(CSV_DIR)
        node_types = [os.path.splitext(file)[0] for file in csv_files]

        LOGGER.info("Setting uniqueness constraints on nodes")
        neo4j_loader.set_constraints(node_types)

        # LOGGER.info("Loading nodes from CSV files")
        # neo4j_loader.load_nodes(csv_handler, csv_files)

        LOGGER.info("Loading relationships from CSV files")
        relationship_configs = load_relationship_configs('relationships.json')
        neo4j_loader.load_relationships(relationship_configs)

    finally:
        neo4j_loader.close()


if __name__ == "__main__":
    main()
