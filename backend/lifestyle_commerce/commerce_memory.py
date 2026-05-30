# backend/lifestyle_commerce/commerce_memory.py

class CommerceMemory:

    def __init__(self):
        self.memory = {}

    def save_interest(
        self,
        user_id: int,
        category: str
    ):

        self.memory.setdefault(user_id, [])
        self.memory[user_id].append(category)

    def get_interests(self, user_id: int):

        return self.memory.get(user_id, [])


commerce_memory = CommerceMemory()