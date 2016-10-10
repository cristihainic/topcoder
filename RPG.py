class RPG:

    def dieRolls(self, dice):

        min = 0
        max = 0

        for i in dice:
            min += int(i[0])
            max += int(i[0]) * int(i[2])

        average = round((max + min) / 2)

        return min, max, average