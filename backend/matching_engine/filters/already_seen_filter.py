from __future__ import annotations


class AlreadySeenFilter:
    """
    Removes profiles the user has already encountered.
    """

    @staticmethod
    def filter(
        candidates,
        seen_user_ids: set[int],
    ):

        if not seen_user_ids:
            return list(candidates)

        return [
            candidate
            for candidate in candidates
            if candidate.id
            not in seen_user_ids
        ]