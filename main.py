from functions import create_password, encrypting, decrypting

chars = ' 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\]^_`{' \
        '|}~ 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\]^_`{' \
        '|}~'
alphabet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!'

# password = create_password(alphabet)
# print(password)


def main():
    # encrypt = f'{password} <-- {input("Для какого ресурса пароль? ")}'
    key = int(input('Число: 1-62\n'))
    # a = encrypting(encrypt=encrypt, key=key, chars=chars)
    a = input('Строка')
    b = decrypting(sequence=a, key=key, chars=chars)
    # print(a)
    print(b)


if __name__ == '__main__':
    main()
