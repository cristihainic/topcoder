class StairClimb:

    def stridesTaken(self, flights, stairsPerStride):

        strides = (len(flights) - 1) * 2

        for i in range(0, len(flights)):
            strides += flights[i] // stairsPerStride
            if flights[i] % stairsPerStride != 0:
                strides += 1

        return strides