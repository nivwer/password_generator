from password_generator import Password

length = int(input("How many characters do you want in your password? "))
include_special_chars = input("Do you want to include special characters? (y/n) ").lower() == "y"

password = Password(length, include_special_chars)

if password.check_strength():
    print("Your password is:", password.password)
    print("The password is strong")
else:
    print("Your password is:", password.password)
    print("The password is weak.")

encrypted_password = password.encrypt_password()

print("Your encrypted password is:", encrypted_password)