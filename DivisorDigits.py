class DivisorDigits:

    def howMany(self, number):
        self.number = number

        astring = str(self.number)
        self.counter = 0
        for digit in astring:
            if int(digit) != 0:
                if self.number % int(digit) == 0:
                    self.counter += 1
        return self.counter

