#A program to convert temperature from a unit to another...

import sys


usrUnit_opt=input("Enter the unit of temperature you have:\n  C for celsius, \n F for fahrenheit, \n K for kelvin...\n::::~:  ")
usrInput=float(input("Enter the temperature value : "))

usrUnit=usrUnit_opt.upper()

print("The entered temperature is",usrInput,"",usrUnit,".")


usrNeed_opt=input("Enter the unit of temperature you want from the following:\n  C for celsius, \n F for fahrenheit, \n K for kelvin...\n::::~:  ")


usrNeed=usrNeed_opt.upper()

if(usrUnit=="C" and usrNeed=="F"):
    result=(usrInput*1.8)+32
    

elif(usrUnit=="C" and usrNeed=="K"):
    result=usrInput+273.15


elif(usrUnit=="F" and usrNeed=="C"):
    result=(usrInput-32)*(5/9)


elif(usrUnit=="F" and usrNeed=="K"):
    result=((usrInput-32)*(5/9)+273.15)

elif(usrUnit=="K" and usrNeed=="C"):
    result=(usrInput-273.15)


elif(usrUnit=="K" and usrNeed=="F"):
    result=((usrInput-273.15)*1.8)+32


else:
    print("Enter the correct data!!!")
    

print("The converted value is",result,"",usrNeed,".")
