# ETL Learning Project
This is a small project where I try to understand how ETL pipelines work.

The goal is not to build something advanced.
The goal is to learn the basics and do things step by step.


## Current status
Still work in progress.

## What i've done so far
**utils/file_io.py**
Helper functions for loading and saving CSV and JSON files.

**utils/logger.py**
Logger used across all modules.
DEBUG and INFO levels.

**etl/loader.py**
Loads CSV files into pandas DataFrames with dtype casting

**etl/validators.py**
Currently just a very simple validator to check for:
- required columns exist
- primary keys are not null
- primary keys are unique

**etl/pipeline.py**
Orchestrates ETL flow:
- loads the data
- validates schemas and primary keys
- runs transformations
- stops if something goes wrong

**etl/transformer.py**
Joins tables together and checks for missing and mismatched data.


## Example data
The project uses simple example data about sales:
- customers
- products
- orders
- order_items

The files are in:
**data/raw/**

Right now the data is valid.
Later I will break it on purpose for my learning.


## Current Project Structure
```
project/
├── data/
│   └── raw/
│       ├── customers.csv
│       ├── products.csv
│       ├── orders.csv
│       └── order_items.csv
├── etl/
│   ├── loader.py
│   ├── validators.py
│   ├── transformer.py
│   └── pipeline.py
├── utils/
│   ├── file_io.py
│   └── logger.py
├── tests/              # not used yet
├── .gitignore
└── README.md
```

## How to run
From the project root:
    python -m etl.pipeline

- if the data is correct, the pipeline finishes.
- if the data is wrong, the pipeline crashes.
This is expected.


## Why this project exists
This project exists so I can:
- learn how ETL projects are structured
- understand why data validation is important
- practice Python and Git
- learn by making mistakes

This is not a finished project.
Its a learning project.


## Notes
I am not very experienced with writing README's yet.
This file will change as i learn more.

