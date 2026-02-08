from etl.loader import load
from etl.validators import (
    assert_required_colums,
    assert_pk_not_null, 
    assert_pk_unique
)

def run_pipeline() -> None:
    customers = load("customers.csv")

    REQUIRED = {"customer_id", "name", "email", "country"}

    assert_required_colums(customers, REQUIRED, "customers")
    assert_pk_not_null(customers, "customer_id", "customers")
    assert_pk_unique(customers, "customer_id", "customers")

    print("Pipeline OK: customers validated")


if __name__ == "__main__":
    run_pipeline()