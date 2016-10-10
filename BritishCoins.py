class BritishCoins:

    def coins(self, pence):

        pounds = 0
        shillings = 0

        while pence >= 240:
            pounds += 1
            pennies -= 240

        while pence >= 12:
            shillings += 1
            pennies -= 12

        return pounds, shillings, pence

