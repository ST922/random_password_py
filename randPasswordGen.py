import string
import random

# Ask a user for a couple of inputs
length = int(input("Please enter length: "))

print('''What would you like to include in your password?
      1 = Digits
      2 = Letters
      3 = Special Characters
      4 = Submit Password Criteria''')

passList = ''  # Empty string

while (True):
    choice = int(input("Pick a number: "))
    if choice == 1:
        passList += string.digits

    elif choice == 2:
        passList += string.ascii_letters

    elif choice == 3:
        passList += string.punctuation

    elif choice == 4:
        break

    else:
        print("That is not a valid input. Please try again.")

password = []

for i in range(length):
    randomCharacter = random.choice(passList)

    password.append(randomCharacter)

print("Here is your password: " + "".join(password))
