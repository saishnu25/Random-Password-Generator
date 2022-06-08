#Random Password Generator Using Python 

import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEGHIJKLMNOPQRSTUVWXYZ"
symbols = "!@#$%^&*()\/|?."
numbers = "0123456789"

use_for = lower_case + upper_case + symbols + numbers 
password_length = 10

password = "".join(random.sample(use_for, password_length))

print("Your Generated Password is: " + password)
