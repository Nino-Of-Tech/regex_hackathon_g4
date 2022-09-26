import re
email = input("Please enter your email: ")
if not re.match("^[a-z]\.[a-z]+@[a-z]+\.email$", email):
    print("Error! Invalid email.")
else:
  print("Your email is " + email)
