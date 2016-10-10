class Inchworm:

    def lunchtime(self, branch, rest, leaf):

        result = 0

        for i in range(0, branch+1, rest):
            if i % leaf == 0:
                result += 1

        return result



