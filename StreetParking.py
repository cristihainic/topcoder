class StreetParking:

    def freeParks(self, street):

        spots_available = 0

        for i in range(0, len(street)-2):

            if street[i] == '-':
                if street[i+1] != 'B' and street[i+2] != 'B':
                    if street[i+1] != 'S' and street[i-1] != 'S':
                        spots_available += 1

        j = street[-1]
        if j == '-':
            if street[street.index(j) - 1] != 'S':
                spots_available += 1

        return spots_available


