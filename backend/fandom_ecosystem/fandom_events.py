# backend/fandom_ecosystem/fandom_events.py

from datetime import datetime


class FandomEventEngine:

    def upcoming_events(self):

        return [

            {
                "name": "Queer Anime Night",
                "time": datetime.utcnow().isoformat(),
                "type": "virtual"
            },

            {
                "name": "KPop Community Meetup",
                "time": datetime.utcnow().isoformat(),
                "type": "voice_chat"
            }

        ]