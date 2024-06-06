from domain.product import Product
from typing import List, Dict


def map_products(data: List[Dict]) -> List[Product]:
    products = []
    for row in data:
        product = Product(
            name=row.get("name"),
            description=row.get("description"),
            price=row.get("price"),
            quantity=row.get("quantity")
        )
        products.append(product)
    return products


def map_product_statistics(statistic: Dict) -> Dict:
    if statistic:
        return {
            "product_count": statistic.get("product_count"),
            "average_price": statistic.get("average_price"),
            "total_quantity": statistic.get("total_quantity")
        }
    else:
        return None
