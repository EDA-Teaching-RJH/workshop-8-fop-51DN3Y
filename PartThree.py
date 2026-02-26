import re

email = input("Enter Email: ")

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.ac.uk$", email):
    print ("Valid")
else:
    print("Invalid")