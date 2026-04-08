user = {
    'name' : '',
    'password' : '', 
} 

name = ''
password = ''

print('Sign Up')
name1 = input('Enter Username ')
password1 = input('Enter passord ')

name = name1
password = password1
    
user['name'] = name
user['password'] =  password

print('Log In')
name2 = input('Enter Username ')
password2 = input('Enter passord ')

if password != password2 and name != name2:
    print('Log in failed')
else:
    print('Welcome ', name)