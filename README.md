> ⚠️ This repository is currently under development and is not ready for use yet. We're actively working on it.

# Neo4j CSV Importer

The `neo4j-csv-importer` is a Python package designed to import CSV data into a Neo4j database. This package supports loading nodes and relationships from CSV files based on a specified ontology.

## Features

- Load nodes from CSV files into Neo4j
- Load relationships from CSV files into Neo4j
- Configurable via environment variables and external JSON files

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/neo4j-csv-importer.git
    cd neo4j-csv-importer
    ```

2. Install the required packages:
    ```sh
    pip install .
    ```

## Configuration

1. Copy the example environment file and update the values according to your setup:
    ```sh
    cp .env.example .env
    ```

2. Create a `relationships.json` file based on the provided template:
    ```sh
    cp .relationships.example.json relationships.json
    ```

## Usage

1. Update the `.env` file with your Neo4j and CSV directory configurations.

2. Update the `relationships.json` file with your specific relationship configurations.

3. Run the importer:
    ```sh
    python main.py
    ```
