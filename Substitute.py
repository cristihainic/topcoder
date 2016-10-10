class Substitute:

    def getValue(self, key, code):

        decoded = ''

        for letter in code:
            if letter in key:
                to_add = str(key.index(letter) + 1)
                if to_add == '10':
                    to_add = '0'
                decoded += to_add

        return int(decoded)