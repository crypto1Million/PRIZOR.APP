from datetime import datetime


class AgencyEngine:

    def create_agency(
        self,
        owner_id: int,
        agency_name: str
    ):

        return {
            "owner_id": owner_id,
            "agency_name": agency_name,
            "created_at": datetime.utcnow()
        }

    def verify_agency(
        self,
        agency_id: int
    ):

        return {
            "agency_id": agency_id,
            "verified": True
        }


agency_engine = AgencyEngine()