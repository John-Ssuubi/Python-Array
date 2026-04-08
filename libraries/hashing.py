import hashlib

def hash_my_details():
    username = input('enter Username \n')
    userpwd = input('enter password \n')
    digest = hashlib.md5(userpwd.encode()).hexdigest()
    return f'Welcome user {username} and with \npassword {digest}'

print(hash_my_details())