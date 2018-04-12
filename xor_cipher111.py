import argparse
from itertools import cycle


class XORCryptographer:
    def __init__(self, key):
        self.key = key

    def encrypt(self, text):
        try:
            return ''.join(chr(ord(char) ^ ord(k))
                           for char, k in zip(text, cycle(self.key)))
        except TypeError:
            return ''.join(chr(ord(char) ^ self.key) for char in text)

    def decrypt(self, cyphered_text):
        try:
            return ''.join(chr(ord(char) ^ ord(k))
                           for char, k in zip(cyphered_text, cycle(self.key)))
        except TypeError:
            return ''.join(chr(ord(char) ^ self.key) for char in cyphered_text)


if __name__ == '__main__':
    # cryptographer = XORCryptographer(key='s3cr3t')
    # message = 'hello world'
    # cyphered = cryptographer.encrypt(message)
    # print('%s ^ %s = %s' % (message, cryptographer.key, cyphered))
    # decrypted = cryptographer.decrypt(cyphered)
    # print('%s ^ %s = %s' % (cyphered, cryptographer.key, message))

    # to run from command line
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--action', required=True,
                        choices=['encrypt', 'decrypt'],
                        help='Type of action: "encrypt" or "decrypt".')
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
    if args.action == 'encrypt':
        print('Encrypted "{}" to {} using '
              'key {}'.format(args.text,
                              cryptographer.encrypt(args.text),
                              args.key))
    elif args.action == 'decrypt':
        print('Decrypted "{}" to "{}" using '
              'key {}'.format(args.text,
                              cryptographer.encrypt(args.text),
                              args.key))
