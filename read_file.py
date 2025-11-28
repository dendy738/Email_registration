import json

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
