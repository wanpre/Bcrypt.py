from tqdm import tqdm
import bcrypt
import argparse

def crack_password(password, encrypted_password, salt=None):
    if salt:
        encrypted_password = "$2a$07$" + salt

    if bcrypt.checkpw(password.encode('utf-8'), encrypted_password.encode('utf-8')):
        print("Password cracked: " + password)
        return True
    else:
        return False

def main():
    parser = argparse.ArgumentParser(description='Bcrypt password cracker')
    parser.add_argument('-p', '--passwordfile', help='Path to the password file')
    parser.add_argument('-d', '--dictionary', help='Path to the password dictionary file')
    args = parser.parse_args()

    password_dictionary = []

    if args.passwordfile:
        with open(args.passwordfile, 'r') as file:
            lines = file.readlines()
            if len(lines) >= 1:
                password = lines[0].strip()
                salt = lines[1].strip() if len(lines) >= 2 else None

                if args.dictionary:
                    with open(args.dictionary, 'r', encoding='latin-1') as dict_file:
                        password_dictionary = dict_file.read().splitlines()
                else:
                    password_dictionary = ["password", "123456", "qwerty", "admin"]

                for password_guess in tqdm(password_dictionary, desc="Cracking passwords"):
                    if crack_password(password_guess, password, salt):
                        break
            else:
                print("Invalid password file. It should have at least 1 line (password).")
    else:
        print("No password file specified.")

if __name__ == '__main__':
    main()
