from __future__ import annotations


class BlockedFilter:
    """
    Removes users who are blocked by either side.
    """

    @staticmethod
    def filter(
        candidates,
        blocked_user_ids: set[int],
    ):

        if not blocked_user_ids:
            return list(candidates)

        return [
            candidate
            for candidate in candidates
            if candidate.id
            not in blocked_user_ids
        ]