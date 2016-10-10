class CardCount:

    def dealHands(self, numPlayers, deck):

        deck = list(deck)
        result = []
        for i in range(0, numPlayers):
            result.append('')

        if numPlayers <= len(deck):
            while len(deck) > 0:
                for i in range(0, numPlayers):
                    result[i] += deck[0]
                    deck.remove(deck[0])

        return tuple(result)

