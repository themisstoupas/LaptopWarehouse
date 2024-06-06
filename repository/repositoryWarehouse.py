from domain.product import Product
from repository.databaseConnection import DatabaseConnection


class RepositoryWarehouse:
    repositoryWarehouse = DatabaseConnection()

    def create_product(self, product: Product):
        try:
            query = """
            INSERT INTO products (name, description, price, quantity) VALUES
            (%s, %s, %s, %s) RETURNING *
            """
            params = (product.name, product.description, product.price, product.quantity)
            result = self.repositoryWarehouse.execute_query(query, params)
            return result
        except Exception as e:
            print(f"An unexpected error occurred while creating product: {e}")
            return None

    def get_product_by_name(self, name: str):
        query = "SELECT * FROM products WHERE name = %s"
        return self.repositoryWarehouse.fetch_data(query, (name,))

    def get_products(self):
        query = "SELECT * FROM products"
        return self.repositoryWarehouse.fetch_data(query)

    def delete_product(self, name: str):
        try:
            query = "DELETE FROM products WHERE name = %s RETURNING *"
            params = (name,)
            result = self.repositoryWarehouse.execute_query(query, params)
            return result is not None
        except Exception as e:
            print(f"An unexpected error occurred while deleting product: {e}")
            return False

    def update_product(self, name: str, updated_product: Product):
        try:
            current_product_query = "SELECT description, price, quantity FROM products WHERE name = %s"
            current_product = self.repositoryWarehouse.execute_query(current_product_query, (name,))

            if not current_product:
                return None

            updated_description = updated_product.description or current_product['description']
            updated_price = updated_product.price or current_product['price']
            update_quantity = updated_product.quantity or current_product['quantity']

            query = """
            UPDATE products SET
                description = %s,
                price = %s,
                quantity = %s
            WHERE name = %s RETURNING *
            """
            params = (updated_description, updated_price, update_quantity, name)
            result = self.repositoryWarehouse.execute_query(query, params)
            return result
        except Exception as e:
            print(f"An unexpected error occurred while updating product: {e}")
            return None

    def update_stock(self, name: str, quantity: int):
        try:
            query = """
            UPDATE products
            SET quantity = quantity + %s
            WHERE name = %s
            RETURNING *
            """
            params = (quantity, name)
            result = self.repositoryWarehouse.execute_query(query, params)
            return result
        except Exception as e:
            print(f"An unexpected error occurred while updating stock: {e}")
            return None

    def calcul_product_statistics(self):
        try:
            query = """
            SELECT COUNT(*) AS product_count,
                   AVG(price) AS average_price,
                   SUM(quantity) AS total_quantity
            FROM products
            """
            statistic = self.repositoryWarehouse.execute_query(query, None)
            return statistic
        except Exception as e:
            print(f"An unexpected error occurred while calculating product statistics: {e}")
            return None
