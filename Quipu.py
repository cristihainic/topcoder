class Quipu:

    def readKnots(self, knots):

        decoded = 0
        last_found_dash = 0

        for i in range(1, len(knots)):
            if knots[i] == '-':
                decoded = decoded * 10 + (i - last_found_dash - 1)
                last_found_dash = i

        return decoded