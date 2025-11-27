def user_authorization(data, email):
    attempt = 5
    while attempt > 0:
        inputed_pass = input("Enter your password: ")
        if inputed_pass == data[email]:
            print('Authorization successful!')
            return {'is_success': True}
        else:
            attempt -= 1
            print(f'Incorrect password! You have {attempt} attempts left.')
            continue
    return {'is_success': False}



