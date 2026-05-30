# backend/lifestyle_commerce/digital_drops.py

from datetime import datetime


class DigitalDrops:

    def create_drop(
        self,
        creator_id: int,
        title: str
    ):

        return {
            "creator_id": creator_id,
            "title": title,
            "created_at": datetime.utcnow().isoformat()
        }

    def get_active_drops(self):

        return []


digital_drops = DigitalDrops()