import pytest
from neo4j_csv_importer.csv_handler import CSVHandler
from neo4j_csv_importer.neo4j_loader import Neo4jLoader
from pathlib import Path


@pytest.fixture
def csv_handler():
    return CSVHandler(Path().absolute())  # current directory


@pytest.fixture
def mock_neo4j_driver(mocker):
    return mocker.patch('neo4j.GraphDatabase.driver')


@pytest.fixture
def neo4j_loader(mock_neo4j_driver):
    return Neo4jLoader('bolt://localhost:7687', 'neo4j', 'neo4j')
