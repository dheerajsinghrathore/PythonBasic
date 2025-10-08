#   Print year of birth based on user input of age and current year and which year they will turn 100 years old.
age = int(input("Enter your age: "))
current_year = int(input("Enter the current year: "))
year_of_birth = current_year - age
year_turn_100 = year_of_birth + 100
print("Year of Birth:", year_of_birth)
print("You will turn 100 years old in the year:", year_turn_100)

import datetime
current_year = datetime.datetime.now().year     # Get the current year from the system
age = int(input("Enter your age: "))
year_of_birth = current_year - age
year_turn_100 = year_of_birth + 100
print("Year of Birth:", year_of_birth)
print("You will turn 100 years old in the year:", year_turn_100)