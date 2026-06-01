class EventSponsors:

    def add_sponsor(
        self,
        event_id: int,
        brand_id: int
    ):

        return {
            "event_id": event_id,
            "brand_id": brand_id
        }

    def remove_sponsor(
        self,
        sponsor_id: int
    ):

        return True

    def list_sponsors(
        self,
        event_id: int
    ):

        return []


event_sponsors = EventSponsors()