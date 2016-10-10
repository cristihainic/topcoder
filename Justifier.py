class Justifier:

    def justify(self, textIn):

        longest = max([len(word) for word in textIn])
        justified = [' ' * (longest - len(word)) + word for word in textIn]

        return justified

        # longest = 0
        # textIn = list(textIn)
        #
        # for i in textIn:
        #     if len(i) > longest:
        #         longest = len(i)
        #
        # for j in range(0, len(textIn)):
        #     while len(textIn[j]) < longest:
        #         textIn[j] = " " + textIn[j]
        #
        # return textIn





