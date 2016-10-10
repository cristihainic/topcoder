class FormatAmt:

    def amount(self, dollars, cents):

        dollars_formatted = '${:,}'.format(dollars)

        cents_formatted = '{}{}'.format(cents // 10, cents % 10)

        return '{}.{}'.format(dollars_formatted, cents_formatted)

    def __call__(self, dollars, cents):

        return self.amount(dollars, cents)