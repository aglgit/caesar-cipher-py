from argparse import ArgumentParser, BooleanOptionalAction

from cipher import CaesarCipher

if __name__ == '__main__':
    parser = ArgumentParser(
        prog='Caesar cipher',
        description='Takes in a text file as argument and prints encoded/decoded text'
                    'using the Caesar cipher')
    parser.add_argument('-f', '--filename', help='Filename')
    parser.add_argument('-c', '--cipher', help='Cipher value')
    parser.add_argument('-d', '--decode',
                        action=BooleanOptionalAction,
                        help='Include to decode the text')

    args = parser.parse_args()
    filename = args.filename
    cipher = int(args.cipher or 0)
    decode = args.decode

    file = open(filename, "r")
    text = file.read()
    file.close()

    if not decode:
        c = CaesarCipher(cipher)
        enc = c.encode(text)
        print(enc)
    else:
        c = CaesarCipher(cipher)
        dec = c.decode(text)
        print(dec)
