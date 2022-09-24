
import re
User_name = input("Please enter full name: ")
if not re.match(r"^([A-Za-z\d]+)( [A-Za-z\d]+)( [A-Za-z\d]+)$", User_name):
    print("Error! invalid user name")
else:
  print("Your full name is " + User_name)

