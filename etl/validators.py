import pandas as pd
from utils.logger import get_logger

logger = get_logger("etl.validators")

def assert_required_colums(df: pd.DataFrame, required: set[str], table_name: str) -> None:
    logger.debug(f"Checking for required columns in {table_name}")
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"{table_name}: missing required columns: {missing}")
    

def assert_pk_not_null(df: pd.DataFrame, pk: str, table_name: str) -> None:
    logger.debug(f"Checking if primary keys are not null in {table_name}")
    if df[pk].isna().any():
        raise ValueError(f"{table_name}: primary key '{pk}' contains NULL values")
    

def assert_pk_unique(df: pd.DataFrame, pk: str, table_name: str) -> None:
    logger.debug(f"Checking if primary keys are unique in {table_name}")
    duplicates = df[pk][df[pk].duplicated()].unique()
    if len(duplicates) > 0:
        raise ValueError(f"{table_name}: does not have unique primary key '{pk}': \n{duplicates}")
    

def validate_schema(df: pd.DataFrame, required: set[str], pk: str | None, table_name: str) -> None:
    assert_required_colums(df, required, table_name)
    if pk is not None:
        assert_pk_not_null(df, pk, table_name)
        assert_pk_unique(df, pk, table_name)
    logger.info(f"Validation successfull for {table_name}")