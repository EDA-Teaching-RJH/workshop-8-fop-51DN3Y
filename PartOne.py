def main():
    email = input("What's your email address? ").strip()

    if "@" and "." in email:
        print("Valid")
    else:
        print("Invalid Email")
    

main()