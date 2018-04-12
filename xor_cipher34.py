import argparse
from itertools import cycle


class XORCryptographer:
    def __init__(self, key):
        self.key = key

    def convert(self, text):
        try:
            return ''.join(chr(ord(char) ^ ord(k))
                           for char, k in zip(text, cycle(self.key)))
        except TypeError:
            return ''.join(chr(ord(char) ^ self.key) for char in text)


if __name__ == '__main__':
    # cryptographer = XORCryptographer(key='9999999999999999')
    # message = 'hello world'
    # cyphered = cryptographer.convert(message)
    # print('%s ^ %s = %s' % (message, cryptographer.key, cyphered))
    # decrypted = cryptographer.convert(cyphered)
    # print('%s ^ %s = %s' % (cyphered, cryptographer.key, message))

    # to run from command line
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--key', required=True,
                        help='A key to perform encryption or decryption.')
    parser.add_argument('-t', '--text', type=str, required=True,
                        help='A text to encrypt or decrypt.')
    parser.add_argument('--key_to_int', action='store_true',
                        help='Use key as an integer instead of as a string.')
    args = parser.parse_args()
    
    if args.key_to_int:
        args.key = int(args.key)

    cryptographer = XORCryptographer(key=args.key)

    print('Converted "{}" to {} using '
          'key {} .'.format(args.text,
                            cryptographer.convert(args.text),
                            args.key))
