import re

print("Enter the phone number: ")
number = input()
regex = "\d{3}-\d{3}-\d{4}"
if re.search(regex, number):
  print("This is a valid Canadian number")
else:
    print("This is not a valid Canadian number!")