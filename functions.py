from random import choice


def create_password(alphabet):
    return ''.join(choice(alphabet) for _ in range(12))


def encrypting(encrypt, key, chars):
    return ''.join(chars[chars.find(i) + key] if i in chars else i for i in encrypt)


def decrypting(sequence, key, chars):
    return ''.join(chars[chars.find(i) - key] if i in chars else i for i in sequence)
