class RGBColor:

    def getComplement(self, rgb):

        result = [0, 0, 0]

        for i in range(0, len(rgb)):
            result[i] = 255 - rgb[i]
            if result[i] in range(rgb[i]-32, rgb[i]+33):
                if rgb[i] + 128 <= 255:
                    result[i] = rgb[i] + 128
                else:
                    result[i] = rgb[i] - 128

        return result