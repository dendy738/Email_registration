import re
import json
from authorization import user_authorization

_users_path = 'users_email.json'
_denied_users_path = 'denied_users_email.json'

def get_users_database(path):
    try:
        with open(path, 'r') as f:
            try:
                _USERS = json.load(f)
            except json.decoder.JSONDecodeError:
                _USERS = {}
    except FileNotFoundError:
        _USERS = {}
    return _USERS

def get_denied_users(path):
    try:
        with open(path, 'r') as f:
            try:
                denied_emails = json.load(f)
            except json.decoder.JSONDecodeError:
                denied_emails = set()
    except FileNotFoundError:
        denied_emails = set()

    if isinstance(denied_emails, set):
        return denied_emails

    return set(denied_emails.keys())


def check_email(email, data):
    return email in data


denied_users = get_denied_users(_denied_users_path)


def input_user_info(users: dict):
    global denied_users
    email_pattern = r'[a-z0-9.]+@[a-z]+.[a-z]+'
    pass_pattern = r'[@#$%&*=!,()^{}/\~`]+'
    while True:
        user_email = input('Email (must start with a lowercase letter and email can consist lower letters, digits, "."):\n')
        if re.match(email_pattern, user_email):
            if user_email in denied_users:
                return 'You have been denied!'
            else:
                is_exist = check_email(user_email, users)
                if is_exist:
                    response = user_authorization(users, user_email)
                    if response['is_success']:
                        return users
                    else:
                        users.pop(user_email)
                        denied_users.add(user_email)
                        return users
                else:
                    user_password = input('Password (may consist lower letters, digits, symbols - (".+-_"):\n')
                    if re.search(pass_pattern, user_password):
                        print('Password contain forbidden characters.')
                        continue
                    else:
                        users[user_email] = user_password
                        return users
        else:
            print('Invalid name of email or such email is not exist!')
            continue


def dump_emails_to_file(data, path):
    with open(path, 'w') as f:
        json.dump(data, f)


def dump_denied_users_to_file(data, path):
    denied_dict = dict.fromkeys(data, 'Denied')
    with open(path, 'w') as f:
        json.dump(denied_dict, f)


def main():
    users = get_users_database(_users_path)
    users_update = input_user_info(users)
    dump_emails_to_file(users_update, _users_path)
    dump_denied_users_to_file(denied_users, _denied_users_path)

if __name__ == '__main__':
    main()