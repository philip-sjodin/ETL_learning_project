import pandas as pd
from utils.logger import get_logger

logger = get_logger("etl.transformer")

def join_order_items_with_orders(order_items: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    logger.debug("Joining order_items with orders on order_id")

    return order_items.merge(orders, on="order_id", how="left", validate="many_to_one")


def join_orders_items_with_products(order_lines: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    logger.debug("Joining order_lines with products on product_id")

    return order_lines.merge(products, on="product_id", how="left", validate="many_to_one")


def assert_no_orphan_products(order_lines: pd.DataFrame, products: pd.DataFrame) -> None:
    logger.debug("Checking for orphan product_ids")

    if "product_id" not in order_lines.columns:
        raise ValueError("order_lines: 'product_id' column missing")
    
    valid_product_ids = set(products["product_id"])
    orphan_mask = ~order_lines["product_id"].isin(valid_product_ids)

    if orphan_mask.any():
        orphans = order_lines.loc[orphan_mask, ["order_id", "product_id"]]
        raise ValueError(
            f"Orphan product_id detected: {orphans['product_id'].nunique()} missing.\n"
            f"Sample:\n{orphans.head(10)}"
        )
    
def assert_no_orphan_orders(order_items: pd.DataFrame, orders: pd.DataFrame) -> None:
    logger.debug("Checking for orphan order_ids")
    if "order_id" not in order_items.columns:
        raise ValueError("order_items: 'order_id' column missing")
    
    valid_order_ids = set(orders["order_id"])
    orphan_mask = ~order_items["order_id"].isin(valid_order_ids)

    if orphan_mask.any():
        orphans = order_items.loc[orphan_mask, ["order_id", "product_id"]]
        raise ValueError(
            f"Orphan order_id detected: {orphans['order_id'].nunique()} missing.\n"
            f"Sample:\n{orphans.head(10)}"
        )
    

def build_order_lines_dataset(
        orders: pd.DataFrame,
        order_items: pd.DataFrame,
        products: pd.DataFrame,
) -> pd.DataFrame:

    assert_no_orphan_orders(order_items, orders)
    order_lines = join_order_items_with_orders(order_items, orders)
    assert_no_orphan_products(order_lines, products)
    order_lines = join_orders_items_with_products(order_lines, products)

    order_lines["line_total"] = order_lines["quantity"] * order_lines["price"]

    logger.info(f"order_lines built: {len(order_lines)} rows")

    return order_lines