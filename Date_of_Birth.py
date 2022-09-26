#!/usr/bin/python3
import re
User = input("Please enter your date of birth: ")
if not re.match('^(?!(?:29|3[01])[\/\-\._]02[\/\-\._].*)(?!31[\/\-\._](?:04|06|09|11)[\/\-\._].*)(?:(?:0[0-9])|(?:[1-2][0-9])|(?:3[0-1]))([\/\-\._])((?:0[1-9])|(?:1[0-2]))([\/\-\._])(\d{4})$', User):
    print("Misprint! Invalid date of birth.")
else:
    print("Your date of birth is " + User)
