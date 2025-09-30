# ======================================================
# Hello User APP
# Author: Faiz Ur Rehman Ashrafi
# Description:
#   A simple interactive Python program that takes user
#   input (name, age, city, etc.), prints a styled intro
#   using colored text (via Colorama), and optionally
#   saves the details into a text file.
# ======================================================

import datetime
from colorama import init, Fore, Style

# Initialize Colorama (for cross-platform colored output)
# autoreset=True ensures colors reset automatically after use
init(autoreset=True)

# ----------------------------
# Collecting user information
# ----------------------------
name = input("Enter Your Good Name: ")

# Handle invalid or negative age input safely
try:
    age = int(input("Enter Your Age: "))
    if age <= 0:
        raise ValueError("Please Enter Age in Positive Number: ")
except ValueError:
    print("Invalid Age! Please Enter a Number: ")
    exit()

# Calculate next year's age
next_age = age + 1

# Ask for more personal details
city = input("Enter Your City: ")
country = input("Enter Your Country: ")
qualification = input("Enter Your Qualification: ")
color = input("Enter Your Favorite Color: ")
hobbies = input("Enter Your Hobbies: ")
foods = input("Enter Your Favorite Foods: ")
goal = input("Enter Your Future Dream: ")

# Get current timestamp (to log file creation time)
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# ----------------------------
# Prepare formatted output
# ----------------------------
data = f"""Hello! Everyone
My Name is {Fore.BLUE}{name}{Style.RESET_ALL}.
I am {age} years old.
Next Year I will be {Fore.CYAN}{next_age}{Style.RESET_ALL}.
I live in {city}, {country}.
I have done {Fore.GREEN}{qualification}{Style.RESET_ALL}.
My favorite color is {color}.
I spend my daily times in {hobbies}.
I love {foods}.
I want to become {Fore.MAGENTA}{goal}{Style.RESET_ALL}.
Thanks for everyone and I will see you next time.
"""

# Display the introduction on console
print(data)

# Add timestamp information to file data
data += f"\nThis file was created on {Fore.YELLOW}{timestamp}{Style.RESET_ALL}\n"

# ----------------------------
# Ask user for permission to save data
# ----------------------------
get_permission = input("Do you want to save file? Type Yes or No: ")

# If user agrees, write data into a text file
if get_permission.lower() == "yes":
    # Save as "hello_<name>.txt"
    with open(f"hello_{name}.txt", "w+", encoding="utf-8") as f:
        f.write(data)  # Write all collected data
        f.seek(0)  # Reset file pointer to beginning

        # Print saved file content back to console
        print("\n" + "-" * 40)
        for line in f:
            print(line, end="")
        print("\n" + "-" * 40)

# ======================================================
# End of Program
# ======================================================
