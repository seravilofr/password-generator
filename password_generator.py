import random

# Set of possible characters
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
symbols = '!@#$%^&*()_+-=[]{}|;:,.<>/?'

# Combine all characters into a single string
def generate_password(length):
    all_characters = uppercase_letters + lowercase_letters + digits + symbols
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

#Ask the user for the password length
while True:
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 5:
            print("Invalid input. Your password must be at least 6 characters long.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Generate and print the password
generated_password = generate_password(length)
print("Your new password is:", generated_password)
