username = input('User name: ')
password = input('Password: ')
password_len = len(password)
password_star = '*' * password_len

print(f'{username}, your password {password_star} is {password_len} letters long')
