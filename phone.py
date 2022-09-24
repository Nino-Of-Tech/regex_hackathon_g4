import re
phone = input("Please enter your phone number: ")
if not re.match(r"(\+\d{3})[\s|\-]\d{3}[\s|\-]\d{3}[\s|\-]\d{3}", phone):
    print("Error! invalid phone")
else:
  print("Your phone number is " + phone)


