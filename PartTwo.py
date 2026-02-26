import re

email = input("Enter Email: ")

if re.search("@", email):
    print ("Valid")