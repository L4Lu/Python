# Python password strength checker
# Written as part of my learning path.

pass_strength = True
user_password = input("Password: ")

if len(user_password) < 8:
    print("Password must be at least 8 characters")
    pass_strength = False

if user_password.islower():
    print("Password does not contain uppercase letters")
    pass_strength = False

if user_password.isupper():
    print("Password does not contain lowercase letters")
    pass_strength = False

if user_password.isdigit():
    print("Password does not contain lowercase or uppercase letters")
    pass_strength = False

if any(char.isdigit() for char in user_password) == 0:
    print("Password must contain at least 1 digit")
    pass_strength = False

if pass_strength == True:
    print("Password is strong")
else:
    print("Password is weak")
