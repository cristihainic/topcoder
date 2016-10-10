class GuessTheNumber:

    def noGuesses(self, upper, answer):

        lower = 1
        guess = int((lower + upper) / 2)
        tries = 1

        while guess != answer:
            tries += 1
            if guess < answer:
                lower = guess + 1
            elif guess > answer:
                upper = guess - 1
            guess = int((lower + upper) / 2)

        return tries