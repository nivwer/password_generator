import random
import string
import hashlib

class Password:
    def __init__(self, length, include_special_chars):
        self.length = length
        self.include_special_chars = include_special_chars
        self.password = self.generate_password()

    def check_strength(self):
        # Check the strength of the password based on criteria such as length, complexity, etc.
        # Return True if the password is strong enough, False otherwise.
        if len(self.password) >= 8 and any(char.isdigit() for char in self.password) and any(char.isupper() for char in self.password) and any(char.islower() for char in self.password):
            return True
        else:
            return False

    def generate_password(self):
        # Generate a random password.
        if self.include_special_chars:
            characters = string.ascii_letters + string.digits + string.punctuation
        else:
            characters = string.ascii_letters + string.digits
        password = "".join(random.choice(characters) for i in range(self.length))
        return password

    def encrypt_password(self):
        # Encrypt the password using the SHA256 algorithm.
        hashed_password = hashlib.sha256(self.password.encode()).hexdigest()
        return hashed_password

