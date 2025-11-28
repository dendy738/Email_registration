import re
from authorization import user_authorization
from read_file import get_users_database, get_denied_users
from put_in_file import dump_emails_to_file, dump_denied_users_to_file
from random_password import password_generator

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
            if user_email in denied_users:
                print('You have been denied!')
                return users

            is_exist = check_email(user_email, users)
            if is_exist:
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
                choice = input('Do you want to create your own password? (Yes/No): ')
                if choice[0] == 'Y':
                    user_password = input('Password (may consist letters, digits, symbols - (.+-_):\n')
                    if re.search(pass_pattern, user_password):
                        print('Password contain forbidden characters.')
                        continue
                    else:
                        users[user_email] = user_password
                        return users
                elif choice[0] == 'N':
                    password_length = int(input('Enter password length (8-18): '))
                    if password_length < 8 or password_length > 18:
                        rand_pass = password_generator()
                        print(f'Your password: {rand_pass}')
                        users[user_email] = rand_pass
                        return users
                    else:
                        rand_pass = password_generator(password_length)
                        print(f'Your password: {rand_pass}')
                        users[user_email] = rand_pass
                        return users
                else:
                    print('Please only choice from Yes/No.')
                    continue
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