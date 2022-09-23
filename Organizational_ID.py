import re
org_ID = input("Please enter your org ID: ")
if not re.match("^\d*[^A-Z][a-z]+$", org_ID):
    print("Error! Invalid org ID")
else:
  print("Your organization ID is " + org_ID)
