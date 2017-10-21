#! /usr/bin/env python3

attempts = 0
attempts_max = 4

def get_auth_details():
    name = input("enter your name ")
    password = input("enter your password ")
    return [name, password]

def password_is_valid(password):
    return password == '123456'

while True:
    if attempts >= attempts_max:
        print("no trying again")
        break;
    else:
        attempts +=1
        details = get_auth_details()
        if password_is_valid(details[1]):
           print("welcome {0}".format(details[0]))
           break;
        else:
            print("please try again")
            print("you are remaining with {0} attempts".format(attempts_max - attempts))
 
# name = input("enter your name ")
# password = input("enter your password ")