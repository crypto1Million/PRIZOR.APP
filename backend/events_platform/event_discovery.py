from typing import List, Dict


class EventDiscovery:

    def discover_nearby_events(
        self,
        city: str
    ) -> List[Dict]:

        return []

    def discover_fandom_events(
        self,
        fandom: str
    ) -> List[Dict]:

        return []

    def discover_creator_events(
        self,
        creator_id: int
    ) -> List[Dict]:

        return []

    def discover_trending_events(self):

        return []


event_discovery = EventDiscovery()