import re
import json


_users_path = 'users_email.json'

def get_users_database(path):
    with open('users_email.json', 'r') as f:
        try:
            _USERS = json.load(f)
        except json.decoder.JSONDecodeError:
            _USERS = {}
    return _USERS


def check_email(email, data):
    return email in data


def input_user_info(users: dict):
    email_pattern = r'[a-z0-9.]+@[a-z]+.[a-z]+'
    pass_pattern = r'[@#$%&*=!,()^{}/\~`]+'
    while True:
        user_email = input('Email (must start with a lowercase letter and email can consist lower letters, digits, "."):\n')
        if re.match(email_pattern, user_email):
            is_exist = check_email(user_email, users)
            if is_exist:
                print('Email already registered.')
            else:
                user_password = input('Password (may consist lower letters, digits, symbols - (".+-_"):\n')
                if re.search(pass_pattern, user_password):
                    print('Password contain forbidden characters.')
                    continue
                else:
                    users[user_email] = user_password
                    break
        else:
            print('Invalid name of email or such email is not exist!')
            continue


def dump_data_to_file(data, path):
    with open(path, 'w') as f:
        json.dump(data, f)


def main():
    users = get_users_database(_users_path)
    input_user_info(users)
    dump_data_to_file(users, _users_path)

if __name__ == '__main__':
    main()