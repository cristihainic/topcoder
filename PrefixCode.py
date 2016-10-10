class PrefixCode:

    def isOne(self, words):

        word_index = []

        for i in words:
            for j in words:
                if i != j:
                    if j.startswith(i):
                        word_index.append(words.index(i))

        if word_index:
            return "No, {}".format(min(word_index))
        else:
            return "Yes"