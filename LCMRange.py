class LCMRange:

    def lcm(self, first, last):

        divide_by = [i for i in range(first, last+1)]

        possible_multiples = [x for x in range(0, 500000)]

        multiples = []

        for i in possible_multiples:
            if all(i % n == 0 and i > last for n in divide_by):
                multiples.append(i)

        return min(multiples)
