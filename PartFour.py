import re

email = input("Enter Email: ")

if re.search(r"^\w+@\w.+\.(ac.uk | gov.uk | nhs.net)$", email):
    print ("Valid")
else:
    print("Invalid")