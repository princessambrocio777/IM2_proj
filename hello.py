# A simple Python program

# Ask for the user's name
name = input("What is your name? ")

# Ask for the user's age
age = int(input("How old are you? "))

# Calculate the year when the user will turn 100
from datetime import datetime
current_year = datetime.now().year
year_100 = current_year + (100 - age)

# Display the result
print(f"Hello, {name}! You will turn 100 years old in the year {year_100}.")
