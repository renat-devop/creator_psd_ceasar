from functions import create_password, encrypting, decrypting

chars = ' 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\]^_`{' \
        '|}~ 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\]^_`{' \
        '|}~'
alphabet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!'


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
              "Try again")


def encrypt():
    password = create_password(alphabet)
    encrypt_var = f'{password} <-- {input("What resource is the password for? ")}'
    key = int(input('Number: 1-62\n'))
    encrypted_password = encrypting(encrypt=encrypt_var, key=key, chars=chars)
    print(f"Your password --> {password} \n"
          f"Encrypted password --> {encrypted_password}")


def decrypt():
    key = int(input('Number: 1-62\n'))
    string = input('Encrypted password \n')
    decrypted_password = decrypting(sequence=string, key=key, chars=chars)
    print(decrypted_password)


if __name__ == '__main__':
    main()
