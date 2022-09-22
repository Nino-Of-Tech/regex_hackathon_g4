
import re
User_name = input("Please enter full name: ")
if not re.match("^[a-zA-Z0-9]{1,30}(?: [a-zA-Z0-9]+)?(?: [a-zA-Z0-9]+)?$", User_name):
    print("Error! invalid email")
else:
  print("Your full name is " + User_name)

