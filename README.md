# Password Generator


## Usage

To use the main.py module, follow these steps:

1. Download or clone the repository that contains the main.py and password_generator.py files.
1. Open a terminal window and navigate to the directory that contains the files using the cd command.
1. Run the main.py module using the command python main.py.
1. The program will prompt you for input. Enter the desired length of the password and whether special characters should be included or not.
1. The program will generate a random password that meets the specified criteria and check its strength. It will then encrypt the password using the SHA256 algorithm and print the generated password, its strength, and the encrypted password to the console.


Here's an example of how to use the main.py module:

```
python main.py
```

The program will prompt you for input:
```
How many characters do you want in your password? 12
Do you want to include special characters? (y/n) y

```

Enter the desired length of the password and whether special characters should be included or not. The program will generate a random password that meets the specified criteria, check its strength, and encrypt it using the SHA256 algorithm. Finally, the program will print the generated password, its strength, and the encrypted password to the console:
```
Your password is: zVgJ~X9Z6R+n
The password is strong
Your encrypted password is: 1e3c3a75e49a79b3476d2c6b7f61512ee1d83a93af8b672a89a1d1f80c02e79a


```