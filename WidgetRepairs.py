class WidgetRepairs:

    def least_days(self, x, y):
        if x < y:
            return x
        else:
            return y

    def days(self, arrivals, numPerDay):

        to_repair = 0
        workdays = 0

        for i in arrivals:
            to_repair += i
            if to_repair > 0:
                workdays += 1
            to_repair -= self.least_days(to_repair, numPerDay)

        while to_repair > 0:
            workdays += 1
            to_repair -= numPerDay

        return workdays