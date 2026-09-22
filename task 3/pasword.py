# PASSWORD GENERATOR

import random
import string

print("========== PASSWORD GENERATOR ==========")

length = int(input("Enter the password length: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    password = password + random.choice(characters)

print("\nGenerated Password:", password)