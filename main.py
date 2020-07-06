from functions import create_password, encrypting, decrypting

chars = ' 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\]^_`{' \
        '|}~ 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\]^_`{' \
        '|}~'
alphabet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!'

password = create_password(alphabet)


# print(password)


def main():
    try:
        num = int(input("Choose the number \n" +
                        "1) Create and encrypt password \n" +
                        "2) Decrypt password \n"))
        if num == 1:
            encrypt()
        elif num == 2:
            decrypt()
        elif type(num) is int:
            print("Wrong choice\n" +
                  "Choose 1 or 2")
    except ValueError:
        print("Value error\n" +
              "You must use numbers")


def encrypt():
    encrypt_var = f'{password} <-- {input("What resource is the password for?")}'
    print()
    key = int(input('Number: 1-62\n'))
    print(encrypting(encrypt=encrypt_var, key=key, chars=chars))


def decrypt():
    key = int(input('Number: 1-62\n'))
    string = input('String')
    decrypting(sequence=string, key=key, chars=chars)


if __name__ == '__main__':
    main()
