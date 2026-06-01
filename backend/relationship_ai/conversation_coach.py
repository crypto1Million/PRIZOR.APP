class ConversationCoach:

    def suggest_reply(
        self,
        last_message: str
    ):

        if "movie" in last_message.lower():
            return "Ask about their favorite movie."

        if "music" in last_message.lower():
            return "Ask what artist they listen to most."

        return "Ask an open-ended question."


conversation_coach = ConversationCoach()