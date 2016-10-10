class FoxAndSightseeing:

    def getMin(self, position):

        #  calculate distance if skipping city 1..

        position_list = list(position)
        position_list.remove(position_list[1])
        distance = 0
        for i in range(0, len(position_list)-1):
            distance += abs(position_list[i] - position_list[i+1])

        #  if more cities, do the same with them aftwrwards

        if len(position) > 3:
            for i in range(0, len(position)-1):
                iter_list = list(position)
                iter_list.remove(iter_list[i])
                iter_distance = 0
                for j in range(0, len(iter_list)-1):
                    iter_distance += abs(iter_list[j] - iter_list[j+1])

            # while comparing with initial distance.
                if iter_distance < distance:
                    distance = iter_distance

        return distance




