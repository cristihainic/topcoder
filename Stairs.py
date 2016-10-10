class Stairs:

    def designs(self, maxHeight, minWidth, totalHeight, totalWidth):

        designs = 0

        for i in range(1, maxHeight):
            for j in range(minWidth, totalWidth):
                if totalHeight % i == 0:
                    if totalWidth % j == 0:
                        if totalHeight / i - 1 == totalWidth / j:
                            designs += 1

        return designs


