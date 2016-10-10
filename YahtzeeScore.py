"""
This task is about the scoring in the first phase of the die-game Yahtzee, where five dice are used.
The score is determined by the values on the upward die faces after a roll. The player gets to choose a value,
and all dice that show the chosen value are considered active. The score is simply the sum of values on active dice.
Say, for instance, that a player ends up with the die faces showing 2, 2, 3, 5 and 4. Choosing the value two makes the
dice showing 2 active and yields a score of 2 + 2 = 4, while choosing 5 makes the one die showing 5 active, yielding a
score of 5. Your method will take as input a tuple (integer) toss, where each element represents the upward face of a
die, and return the maximum possible score with these values.
"""

from collections import Counter

class YahtzeeScore:

    def maxPoints(self, toss):

        # search for maximum value
        biggest = 0
        for i in toss:
            if i > biggest:
                biggest = i

        # see if there are any duplicates and calculate maximum sum
        counter = dict(Counter(toss))
        duplicates = 0
        temp_list = []
        for k, v in counter.items():
            if v > 1:
                temp_list.append(k*v)
        for i in temp_list:
            if i > duplicates:
                duplicates = i

        # return whatever value is bigger (either biggest or duplicates)
        if biggest > duplicates:
            return biggest
        else:
            return duplicates