from setuptools import setup, find_packages

setup(
    name='neo4j_csv_importer',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'neo4j==5.21.0',
        'pandas==2.2.2',
        'python-dotenv==1.0.1',
        'retry==0.9.2'
    ],
    entry_points={
        'console_scripts': [
            'neo4j_csv_importer=neo4j_csv_importer.main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
