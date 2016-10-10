"""
Julius Caesar used a system of cryptography, now known as Caesar Cipher, which shifted each letter 2 places further
 through the alphabet (e.g. 'A' shifts to 'C', 'R' shifts to 'T', etc.). At the end of the alphabet we wrap around,
  that is 'Y' shifts to 'A'.
We can, of course, try shifting by any number. Given an encoded text and a number of places to shift, decode it.
For example, "TOPCODER" shifted by 2 places will be encoded as "VQREQFGT". In other words, if given (quotes for clarity)
 "VQREQFGT" and 2 as input, you will return "TOPCODER". See example 0 below.
"""


class CCipher:

    def decode(self, cipherText, shift):

        self.cipherText = list(cipherText)
        self.shift = shift
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * 10
        temp_list = []
        decoded = []
        i = 0

        for letter in self.cipherText:
            decoded.append('')
            temp_list.append(alphabet.index(letter) - shift)

        while i < len(temp_list):
            decoded[i] = alphabet[temp_list[i]]
            i += 1
        return ''.join(decoded)
