# backend/ai_companion/memory_engine.py

from datetime import datetime


# =====================================================
# MEMORY ENGINE
# =====================================================

class MemoryEngine:

    def __init__(self):

        self.name = "AI Companion Memory Engine"

        # Temporary in-memory storage
        # Replace later with PostgreSQL / Redis
        self.user_memory = {}

    # =================================================
    # CREATE USER MEMORY SPACE
    # =================================================

    def initialize_user(self, user_id: int):

        if user_id not in self.user_memory:

            self.user_memory[user_id] = {
                "preferences": [],
                "important_topics": [],
                "emotional_state": [],
                "conversation_history": [],
                "created_at": str(datetime.utcnow())
            }

    # =================================================
    # STORE USER PREFERENCE
    # =================================================

    def remember_preference(
        self,
        user_id: int,
        preference: str
    ):

        self.initialize_user(user_id)

        if preference not in self.user_memory[user_id]["preferences"]:

            self.user_memory[user_id]["preferences"].append(
                preference
            )

    # =================================================
    # STORE IMPORTANT TOPIC
    # =================================================

    def remember_topic(
        self,
        user_id: int,
        topic: str
    ):

        self.initialize_user(user_id)

        if topic not in self.user_memory[user_id]["important_topics"]:

            self.user_memory[user_id]["important_topics"].append(
                topic
            )

    # =================================================
    # STORE EMOTIONAL STATE
    # =================================================

    def store_emotion(
        self,
        user_id: int,
        emotion: str
    ):

        self.initialize_user(user_id)

        self.user_memory[user_id]["emotional_state"].append({

            "emotion": emotion,
            "timestamp": str(datetime.utcnow())
        })

    # =================================================
    # STORE CONVERSATION
    # =================================================

    def store_conversation(
        self,
        user_id: int,
        user_message: str,
        ai_response: str
    ):

        self.initialize_user(user_id)

        self.user_memory[user_id]["conversation_history"].append({

            "user_message": user_message,
            "ai_response": ai_response,
            "timestamp": str(datetime.utcnow())
        })

    # =================================================
    # GET USER MEMORY
    # =================================================

    def get_memory(
        self,
        user_id: int
    ):

        self.initialize_user(user_id)

        return self.user_memory[user_id]

    # =================================================
    # GET USER PREFERENCES
    # =================================================

    def get_preferences(
        self,
        user_id: int
    ):

        self.initialize_user(user_id)

        return self.user_memory[user_id]["preferences"]

    # =================================================
    # GET LAST EMOTION
    # =================================================

    def get_last_emotion(
        self,
        user_id: int
    ):

        self.initialize_user(user_id)

        emotions = self.user_memory[user_id]["emotional_state"]

        if not emotions:
            return None

        return emotions[-1]

    # =================================================
    # CLEAR MEMORY
    # =================================================

    def clear_memory(
        self,
        user_id: int
    ):

        if user_id in self.user_memory:

            del self.user_memory[user_id]

            return True

        return False


# =====================================================
# SINGLETON INSTANCE
# =====================================================

memory_engine = MemoryEngine()