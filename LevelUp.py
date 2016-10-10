class LevelUp:

    def toNextLevel(self, expNeeded, received):

        needed = 0

        for reqs in expNeeded:
            if reqs <= received:
                expNeeded.remove(reqs)
            if reqs > received:
                needed += reqs - received
                break

        return needed