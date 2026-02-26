import re

email = input("Enter Email: ")

if re.search(r".+@.+\.ac.uk", email):
    print ("Valid")
else:
    print("Invalid")