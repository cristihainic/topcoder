class ProgressBar:

    def showProgress(self, taskTimes, tasksCompleted):

        executed = 0
        for i in range(0, len(taskTimes)):
            if i < tasksCompleted:
                executed += taskTimes[i]

        expected = sum(taskTimes)

        percent_completed = int((executed / expected) * 20)

        result = '#' * percent_completed
        while len(result) < 20:
            result += '.'

        return result






