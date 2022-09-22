import re
User = input("Please enter your username: ")
if not re.match("(^[A-Z]([a-z]*[A-Z])[a-z]*$)", User):
    print("Misprint! invalid Username")
else:
    print("Your user name is " + User)

