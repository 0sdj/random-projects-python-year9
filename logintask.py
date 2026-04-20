#Login Details Code
key = input("The activation key is 978254872 ")
while key not in ("Thanks", "Ok", "OK", "THANKS", "ok"):
    key = input("Say Thanks or Ok at least -some people these days, AI would never- : ")

actkey = input("What is the 9 digit activation key I sent you? ")

while actkey != "978254872":
    actkey = input("Error, key not correct try again: ")

username = input("Activation key correct. Make your username: ")
password = input("What do you want your password to be? ")

print("You have succesfully created your account...")

retype = input("Please login with your details, Username: ")
while retype != username:
    retype = input("Username not correct try again: ")

retype = input("Password: ")
while retype != password:
    retype = input("Sumthn aint right, try again: ")
    
print("Well done you logged in you big baby!")

#Made by Aleks
