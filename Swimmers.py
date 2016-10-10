class Swimmers:

    def getSwimTimes(self, distances, speeds, current):

        times = [0 for i in distances]

        for swimmer in range(0, len(distances)):
            if speeds[swimmer] <= current:
                times[swimmer] = -1
            else:
                with_current = distances[swimmer] / (speeds[swimmer] + current)
                against_current = distances[swimmer] / (speeds[swimmer] - current)
                times[swimmer] += round(with_current + against_current)

        return times

