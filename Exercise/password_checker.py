# Password Checker

Username = input("Username: ")
password = input("Password ")

password_length = len(password)
hidden_password = '*' * password_length

print(f"{Username}, password {hidden_password} is {password_length} letters long")