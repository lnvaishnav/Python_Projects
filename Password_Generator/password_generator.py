import random
import re
import pyhibp
from pyhibp import pwnedpasswords as pw

letters_low = "abcdefghijklmnopqrstuvwxyz"
letters_up = letters_low.upper()
numbers = "0123456789"
symbolls = "!@#$%^&*()_+=-+/`~|"
user_password = "Temp"

mixing = letters_low + letters_up + numbers + symbolls

def user_password_fn():
    length = int(input("Enter the length for you password: "))
    user_password = "".join(random.sample(mixing, length))
    print(f"Your password: {user_password}")
user_password_fn()

pyhibp.set_user_agent(ua="None")
resp = pw.is_password_breached(password=f"{user_password}")

if resp:
    print(f"Password breached! \nThis password was used {resp} times before.")
if int(len(user_password)) <8:
    again = int(input("Your password's length is less than 8. Please re-enter the password.\nEnter 1 to continue..."))
    if again == 1:
        while True:
            user_password_fn()
            z = input("Enter '1' if you want to continue, to exit, enter anything!!!")
            if  '1' not in z:
                break
else:
    print("This password is not breached! \nYou can use this password")