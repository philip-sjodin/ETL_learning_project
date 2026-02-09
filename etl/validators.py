import pandas as pd

def assert_required_colums(df: pd.DataFrame, required: set[str], table_name: str) -> None:
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"{table_name}: missing required columns: {missing}")
    

def assert_pk_not_null(df: pd.DataFrame, pk: str, table_name: str) -> None:
    if df[pk].isna().any():
        raise ValueError(f"{table_name}: primary key '{pk}' contains NULL values")
    

def assert_pk_unique(df: pd.DataFrame, pk: str, table_name: str) -> None:
    if not df[pk].is_unique:
        duplicates = df[pk][df[pk].duplicated()].unique()
        raise ValueError(f"{table_name}: does not have unique primary key '{pk}': \n{duplicates}")
    

def validate_schema(df: pd.DataFrame, required: set[str], pk: str, table_name: str) -> None:
    assert_required_colums(df, required, table_name)
    assert_pk_not_null(df, pk, table_name)
    assert_pk_unique(df, pk, table_name)