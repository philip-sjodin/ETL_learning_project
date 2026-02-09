from etl.loader import load
from etl.validators import validate_schema
from etl.transformer import build_order_lines_dataset


def run_pipeline() -> None:
    orders = load("orders.csv", dtypes={"order_id": int, "customer_id": int})
    products = load("products.csv", dtypes={"product_id": int, "price": float})
    order_items = load("order_items.csv", dtypes={"order_id": int, "product_id": int, "quantity": int})
    customers = load("customers.csv", dtypes={"customer_id": int})

    validate_schema(
        customers, 
        required={"customer_id", "name", "email"}, 
        pk="customer_id", 
        table_name="customers"
    )
    validate_schema(
        orders, 
        required={"order_id", "customer_id", "order_date"}, 
        pk="order_id", 
        table_name="orders"
    )
    validate_schema(
        products, 
        required={"product_id", "name", "price"}, 
        pk="product_id", 
        table_name="products"
    )
    validate_schema(
        order_items,
        required={"order_id", "product_id", "quantity"},
        pk=None,
        table_name="order_items",
    )

    order_lines = build_order_lines_dataset(
        orders=orders, order_items=order_items, products=products,
    )

    print("Pipeline OK")


if __name__ == "__main__":
    run_pipeline()
