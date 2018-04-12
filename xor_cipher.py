import argparse
from itertools import cycle


def xor_convert(text, key):
    try:
        return ''.join(hex(ord(char) ^ ord(k)) for char, k in zip(text, cycle(key)))
    except TypeError:
        return ''.join(hex(ord(char) ^ key) for char in text)


if __name__ == '__main__':
    key = 'sfsgjj'
    message = 'hello world'
    cyphered = xor_convert(message, key)
    with open('file1.txt', 'w') as file:
        file.write(cyphered)
    print('%s ^ %s = %s' % (message, key, cyphered))

    with open('file1.txt', 'r') as file:
        content = file.read()
    decrypted = xor_convert(content, key)
    print('%s ^ %s = %s' % (content, key, message))

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
