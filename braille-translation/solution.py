from collections import OrderedDict

def getlexicon(s, c):
    lexicon = OrderedDict()
    binchars = [c[start:start+6] for start in range(0, len(c), 6)]
    # print(binchars)

    while "000001" in binchars:
        binchars.remove("000001")

    for i, bin in enumerate(binchars):
        lexicon[s[i]] = bin

    # lexsorted = OrderedDict(sorted(lexicon.items()))
    print(lexicon)


def solution(s):
    # Solution goes here
    lexicon = {'t': '011110',  'h': '110010',  'e': '100010',  ' ': '000000',  'q': '111110',  'u': '101001',  'i': '010100',  'c': '100100',  'k': '101000',  'b': '110000',  'r': '111010',  'o': '101010',  'w': '010111',  'n': '101110',  'f': '110100',  'x': '101101',  'j': '010110',  'm': '101100',  'p': '111100',  's': '011100',  'v': '111001',  't': '011110',  'l': '111000',  'a': '100000',  'z': '101011',  'y': '101111',  'd': '100110',  'g': '110110'}
    binchar = ""
    for c in s:
        if c.isupper():
            binchar += "000001"
        binchar += lexicon[c.lower()]

    return binchar

def main():
    # getlexicon("code", "100100101010100110100010")
    # getlexicon("Braille", "000001110000111010100000010100111000111000100010")
    # getlexicon("The quick brown fox jumps over the lazy dog", "000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110")

    # Test case 1
    output = solution("code")
    if output == "100100101010100110100010":
        print("Pass!")
    else:
        print("Fail!")

    # Test case 2
    output = solution("Braille")
    if output == "000001110000111010100000010100111000111000100010":
        print("Pass!")
    else:
        print("Fail!")

    # Test case 3
    output = solution("The quick brown fox jumps over the lazy dog")
    if output == "000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110":
        print("Pass!")
    else:
        print("Fail!")

if __name__ == "__main__":
    main()