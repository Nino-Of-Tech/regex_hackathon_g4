#!/usr/bin/python3
import re
password = input("Please enter your password: ")
if not re.match("^(?!.*[a-z].*[a-z].*[a-z].*)(?!.*\d.*\d.*\d.*)(?!.*[!@#$%^&*()~].*[!@#$%^&*()~].*[!@#$%^&*()~].*)(?!.*[A-Z].*[A-Z].*[A-Z].*).{8,8}$", password):
    print("Error! invalid password")
else:
  print("Your password is " + password)


