import secrets
from threading import Lock

users = list()
users_lock = Lock()

def register_user(name, number, contacts):
    d = dict()
    d['name'] = name; d['number'] = number; d['contacts'] = contacts
    private_token = secrets.token_hex(4)
    shared_token  = secrets.token_hex(4)
    d['private'] = private_token
    d['shared'] = shared_token
    d['subscribers'] = list()
    users_lock.acquire()
    users.append(d)
    users_lock.release()
    return private_token, shared_token

def subscribe_to_token(shared_token, user_id):
    users_lock.acquire()
    for ud in users:
        if ud['shared'] == shared_token:
            ud['subscribers'].append(user_id)
            users_lock.release()
            return
    else:
        users_lock.release()
        raise IndexError
