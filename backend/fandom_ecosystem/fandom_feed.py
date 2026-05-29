# backend/fandom_ecosystem/fandom_feed.py

class FandomFeed:

    def generate_feed(self, tribe: str):

        return [

            {
                "type": "community_post",
                "title": f"Trending inside {tribe}",
            },

            {
                "type": "event",
                "title": f"Live discussion for {tribe}",
            },

            {
                "type": "creator",
                "title": f"Popular creator in {tribe}",
            }

        ]