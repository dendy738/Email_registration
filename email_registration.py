import re
from authorization import user_authorization
from read_file import get_users_database, get_denied_users
from put_in_file import dump_emails_to_file, dump_denied_users_to_file
import numpy as np


_users_path = 'users_email.json'
_denied_users_path = 'denied_users_email.json'

_USERS = get_users_database(_users_path)
denied_users = get_denied_users(_denied_users_path)


def check_email(email, data):
    '''Function for check existence of email'''
    return email in data


#======== Main registration process ============
def user_registration(users: dict):
    global denied_users
    email_pattern = r'[a-z0-9.]+@[a-z]+.[a-z]+'
    pass_pattern = r'[@#$%&*=!,()^{}/\~`]+'

    while True:
        user_email = input('Email (must start with a lowercase letter and email can consist lower letters, digits, "."):\n')
        if re.match(email_pattern, user_email):
            is_exist = check_email(user_email, users)
            if is_exist:
                if user_email in denied_users:
                    return 'You have been denied!'

                response = user_authorization(users, user_email)
                if response['is_success']:
                    print('Authorization successful!')
                    return users
                else:
                    print('Authorization failed! Account has been blocked!')
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
            print('Invalid name of email!')
            continue


def main():
    users = get_users_database(_users_path)
    users_update = user_registration(users)
    dump_emails_to_file(users_update, _users_path)
    dump_denied_users_to_file(denied_users, _denied_users_path)

if __name__ == '__main__':
    main()