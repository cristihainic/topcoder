class Workshop:

    def pictureFrames(self, pieces):

        pieces = list(pieces)
        result = 0

        for i in range(0, len(pieces)-2):
            for j in range(i+1, len(pieces)-1):
                for k in range(j+1, len(pieces)):
                    if pieces[i] + pieces[j] > pieces[k]:
                        if pieces[i] + pieces[k] > pieces[j]:
                            if pieces[j] + pieces[k] > pieces[i]:
                                result += 1

        return result

