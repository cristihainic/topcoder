class TireRotation:

    def getCycle(self, initial, current):

        phases = [
            {initial[0] + initial[1] + initial[2] + initial[3]: 1},
            {initial[3] + initial[2] + initial[0] + initial[1]: 2},
            {initial[1] + initial[0] + initial[3] + initial[2]: 3},
            {initial[2] + initial[3] + initial[1] + initial[0]: 4}
        ]

        state = 0

        for sequence in phases:
            if current in sequence.keys():
                state = sequence[current]
                break
            else:
                state = -1

        return state
