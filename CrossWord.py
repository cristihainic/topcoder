class CrossWord:

    def countWords(self, board, size):

        result = 0
        to_find = '.' * size

        for row in board:
            result += row.count(to_find)
            if (to_find + '.' in row) or ('.' + to_find in row):
                result -= 1

        return result