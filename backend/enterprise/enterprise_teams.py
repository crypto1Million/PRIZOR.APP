class EnterpriseTeams:

    def create_team(
        self,
        organization_id: int,
        name: str
    ):
        return True

    def add_member(
        self,
        team_id: int,
        user_id: int
    ):
        return True


enterprise_teams = EnterpriseTeams()