from repository.repositoryWarehouse import RepositoryWarehouse
from services.mapper import map_products, map_product_statistics
from domain.product import Product


class ProductServices:
    repo_product = RepositoryWarehouse()

    def get_products(self):
        raw_data = self.repo_product.get_products()
        return map_products(raw_data)

    def get_product_by_name(self, name: str):
        raw_data = self.repo_product.get_product_by_name(name)
        return map_products(raw_data)

    def get_product_statistic(self):
        statistic = self.repo_product.calcul_product_statistics()
        return map_product_statistics(statistic)

    def create_product(self, product: Product):
        created_product = self.repo_product.create_product(product)
        return map_products([created_product]) if created_product else None

    def delete_product(self, name: str):
        try:
            return self.repo_product.delete_product(name)
        except Exception as e:
            print(f"An unexpected error occurred while deleting product: {e}")
            return False

    def update_product(self, name: str, updated_product: Product):
        updated_product = self.repo_product.update_product(name, updated_product)
        return map_products([updated_product]) if updated_product else None

    def manage_stock(self, name: str, action: str, quantity: int):
        if action == "increase":
            stock_updated = self.repo_product.update_stock(name, quantity)
        elif action == "decrease":
            stock_updated = self.repo_product.update_stock(name, -quantity)
        else:
            raise ValueError("Invalid action. Must be 'increase' or 'decrease'")
        return map_products([stock_updated]) if stock_updated else None
