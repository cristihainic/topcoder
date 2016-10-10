class EyeDrops:

    def closest(self, sleepTime, k):

        ideal_time_split = 24. / k

        if sleepTime > ideal_time_split:
            return 60 * (24. - sleepTime) / (k - 1)
        else:
            return 60 * ideal_time_split






