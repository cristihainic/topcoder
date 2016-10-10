class ProfitCalculator:

    def percent(self, items):

        sold_for = 0.0
        bought_for = 0.0

        for prices in items:
            sold_for += float(prices[0:6])
            bought_for += float(prices[7:])

        profit = sold_for - bought_for
        margin = int((profit * 100) / sold_for)

        return margin




