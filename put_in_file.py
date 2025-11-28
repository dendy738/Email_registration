import json

def dump_emails_to_file(data, path):
    with open(path, 'w') as f:
        json.dump(data, f)


def dump_denied_users_to_file(data, path):
    denied_dict = dict.fromkeys(data, 'Denied')
    with open(path, 'w') as f:
        json.dump(denied_dict, f)

