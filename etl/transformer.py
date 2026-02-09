import pandas as pd

def join_orders_with_order_items(
        orders: pd.DataFrame, 
        order_items: pd.DataFrame,
) -> pd.DataFrame:
    return orders.merge(order_items, on="order_id", how="left", validate="one_to_many")

def join_orders_items_with_products(order_lines: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    return order_lines.merge(products, on="product_id", how="left", validate="many_to_one")

def assert_no_orphan_products(order_lines: pd.DataFrame, products: pd.DataFrame) -> None:
    if "product_id" not in order_lines.columns:
        raise ValueError("order_lines: 'product_id' column missing")
    
    valid_product_ids = set(products["product_id"])
    orphan_mask = ~order_lines["product_id"].isin(valid_product_ids)

    if orphan_mask.any():
        orphans = order_lines.loc[orphan_mask, ["order_id", "order_item_id", "product_id"]]
        raise ValueError(
            f"Orphan product_id detected: {orphans['product_id'].nunique()} missing.\n"
            f"Sample:\n{orphans.head(10)}"
        )
    

def build_order_lines_dataset(
        orders: pd.DataFrame,
        order_items: pd.DataFrame,
        products: pd.DataFrame,
) -> pd.DataFrame:
    
    order_lines = join_orders_with_order_items(orders, order_items)
    assert_no_orphan_products(order_lines, products)
    order_lines = join_orders_items_with_products(order_lines, products)

    return order_lines