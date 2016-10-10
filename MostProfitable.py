class MostProfitable:

    def convert_int_to_list(self, my_int):

        if type(my_int) == int:
            my_int = [int(x) for x in str(my_int)]

        return my_int

    def bestItem(self, costs, prices, sales, items):

        if type(items) == str:
            items_list = items.split()
        else:
            items_list = list(items)

        costs = self.convert_int_to_list(costs)
        prices = self.convert_int_to_list(prices)
        sales = self.convert_int_to_list(sales)

        values = []

        for i in range(0, len(items_list)):
            values.append((prices[i] - costs[i]) * sales[i])

        if max(values) <= 0:
            return ''
        else:
            return items_list[values.index(max(values))]