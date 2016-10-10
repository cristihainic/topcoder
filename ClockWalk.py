class ClockWalk:

    def finalPosition(self, flips):

        position = 0

        for i in range(0, len(flips)):
            if flips[i] == 'h':
                position = (position + i + 1) % 12
                print("position", position)
            else:
                position = (position - (i + 1) + 120) % 12
                print("position", position)

        if position == 0:
            position = 12

        return position
