class SocialGraph:

    def build_graph(
        self,
        user_id: int,
        friends: list,
        communities: list
    ):

        return {
            "user_id": user_id,
            "friends": friends,
            "communities": communities
        }


social_graph = SocialGraph()