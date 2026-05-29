# backend/fandom_ecosystem/fandom_memory.py

class FandomMemory:

    def __init__(self):

        self.memory = {}

    def save_preferences(self, user_id: int, preferences: dict):

        self.memory[user_id] = preferences

    def get_preferences(self, user_id: int):

        return self.memory.get(user_id, {})