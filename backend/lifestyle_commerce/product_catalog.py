# backend/lifestyle_commerce/product_catalog.py

class ProductCatalog:

    def list_products(self, creator_id: int):

        return [
            {
                "id": 1,
                "name": "Premium Performance Tee",
                "price": 49.99
            }
        ]

    def add_product(
        self,
        creator_id: int,
        product_name: str,
        price: float
    ):

        return {
            "creator_id": creator_id,
            "product_name": product_name,
            "price": price
        }


product_catalog = ProductCatalog()