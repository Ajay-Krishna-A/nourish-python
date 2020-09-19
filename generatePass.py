# A python script to generate passwords according to users' preferences.

import random
import sys    #googled

numbers="0123456789"
charLow="abcdefghijklmnopqrstuvwxyz"
charUp=charLow.upper()

symbols="~!@#$%^&*()_+`-={}\][;':<>,./?"

pass_weak = numbers
pass_medium = numbers + charLow + charUp
pass_strong = pass_medium + symbols


strength =input("Enter the type of password from the following: \n Weak, Medium, Strong:\n:::")

if(strength.lower()=="weak"):
    code=pass_weak
    limit=6
elif(strength.lower()=="medium"):
    code=pass_medium
    limit=12
elif(strength.lower()=="strong"):
    code=pass_strong
    limit=24
else:
    print("Choose the valid option!!!")
    sys.exit()




password="".join(random.sample(code,limit))

print(password)
