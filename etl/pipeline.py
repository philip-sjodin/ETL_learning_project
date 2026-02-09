from etl.loader import load
from etl.validators import validate_schema
from etl.transformer import build_order_lines_dataset


def run_pipeline() -> None:
    customers = load("customers.csv")
    orders = load("orders.csv")
    order_items = load("order_items.csv")
    products = load("products.csv")

    validate_schema(customers, {"customer_id", "name", "email"}, "customer_id", "customers")
    validate_schema(orders, {"order_id", "customer_id", "order_date"}, "order_id", "orders")
    validate_schema(products, {"product_id", "name", "price"}, "product_id", "products")
    validate_schema(
        order_items,
        {"order_item_id", "order_id", "product_id", "quantity"},
        "order_item_id",
        "order_items",
    )

    order_lines = build_order_lines_dataset(
        orders=orders, order_items=order_items, products=products,
    )

    print("Pipeline OK")


if __name__ == "__main__":
    run_pipeline()
