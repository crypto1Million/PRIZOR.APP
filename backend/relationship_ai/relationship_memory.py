class RelationshipMemory:

    def create_memory(
        self,
        topic: str,
        value: str
    ):

        return {
            "topic": topic,
            "value": value
        }


relationship_memory = RelationshipMemory()