class SkipRope:

    def partners(self, candidates, height):

        closest = min(candidates, key=lambda x: x-height)
        candidates.remove(closest)
        next_in_line = min(candidates, key=lambda x: x-closest)

        result = sorted([closest, next_in_line])

        return result