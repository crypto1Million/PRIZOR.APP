class CommunityRecommender:

    def recommend(
        self,
        user_interests,
        communities
    ):

        results = []

        for community in communities:

            if community["topic"] in user_interests:
                results.append(community)

        return results


community_recommender = CommunityRecommender()