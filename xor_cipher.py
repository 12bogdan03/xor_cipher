import argparse
from itertools import cycle


def xor_encrypt(text, key):
    try:
        return ' '.join(hex(ord(char) ^ ord(k))
                        for char, k in zip(text, cycle(key)))
    except TypeError:
        return ' '.join(hex(ord(char) ^ key) for char in text)


def xor_decrypt(cyphered_lst, key):
    try:
        return ''.join(chr(int(char, 16) ^ ord(k))
                       for char, k in zip(cyphered_lst, cycle(key)))
    except TypeError:
        return ''.join(bin(ord(char) ^ key) for char in cyphered)


if __name__ == '__main__':
    key = 'sfsgjj'
    message = 'hello world'
    cyphered = xor_encrypt(message, key)
    with open('file1.txt', 'w') as file:
        file.write(cyphered)
    print('%s ^ %s = %s' % (message, key, cyphered))

    with open('file1.txt', 'r') as file:
        content = file.read().split()
    decrypted = xor_decrypt(content, key)
    print('%s ^ %s = %s' % (content, key, decrypted))

    # to run from command line
    # parser = argparse.ArgumentParser()
    # parser.add_argument('-k', '--key', required=True,
    #                     help='A key to perform encryption or decryption.')
    # parser.add_argument('-t', '--text', type=str, required=True,
    #                     help='A text to encrypt or decrypt.')
    # parser.add_argument('--key_to_int', action='store_true',
    #                     help='Use key as an integer instead of as a string.')
    # args = parser.parse_args()
    #
    # if args.key_to_int:
    #     args.key = int(args.key)
    #
    # print('Converted "{}" to {} using '
    #       'key {} .'.format(args.text,
    #                         xor_convert(args.text, args.key),
    #                         args.key))
