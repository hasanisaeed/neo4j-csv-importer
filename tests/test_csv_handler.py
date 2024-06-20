from pathlib import Path

from neo4j_csv_importer.utils import get_csv_files


def test_get_csv_files():
    directory = Path(__file__).parent
    files = get_csv_files(directory)
    assert len(files) > 0
    assert all(file.endswith('.csv') for file in files)


def test_read_csv(csv_handler):
    csv_file = Path(__file__).parent / 'users.csv'
    data = csv_handler.read_csv(csv_file)
    assert len(list(data)) > 0
