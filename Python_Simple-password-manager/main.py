from cryptography.fernet import Fernet


# write key
def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)


# Load key
def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key


master_pwd = input('What is your master password? \n')
key = load_key() + master_pwd.encode()
fer = Fernet(key)


def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.split('|')
            user, passwd = data[0], data[1]
            print('User:', user, '| Password:', fer.decrypt(passwd.encode()))


def add(**args):
    name = input('Enter your name:\n')
    pwd = input('Enter your password:\n')

    with open('password.txt', 'a') as f:
        f.write(name + '|' + fer.encrypt(pwd.encode()).decode())  # Decode the bytes object to str


while True:
    mode = input('Would you like to add a new password or view the existing password? (add/view) or q to quit\n').lower()
    if mode == 'q':
        break
    elif mode == 'add':
        add()
    elif mode == 'view':
        view()
    else:
        print('invalid mode')
        continue
