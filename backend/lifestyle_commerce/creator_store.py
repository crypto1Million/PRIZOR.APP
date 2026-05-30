# backend/lifestyle_commerce/creator_store.py

class CreatorStore:

    def get_followed_creator_stores(self, user_id: int):

        return [
            {
                "creator_id": 1,
                "store_name": "Auron Performance",
                "category": "Sportswear"
            }
        ]

    def create_store(
        self,
        creator_id: int,
        store_name: str,
        description: str
    ):

        return {
            "creator_id": creator_id,
            "store_name": store_name,
            "description": description
        }


creator_store = CreatorStore()