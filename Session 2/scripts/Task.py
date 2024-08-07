def register_account():
    print("Welcome to Account Registration!")
    
    first_name = input("Enter your First Name: ")
    if first_name.lower() != "samtech":
        print("Sorry, you are not a member of this prestigious company. Try again!")
        return
    
    last_name = input("Enter your Last Name: ")
    username = input("Enter your Username: ")
    email = input("Enter your Email: ")
    
    if "@" not in email or "gmail.com" not in email:
        print("Please enter a valid Gmail email address.")
        return
    
    password = input("Enter your Password: ")
    confirm_password = input("Confirm your Password: ")
    
    if password != confirm_password:
        print("Passwords do not match. Please try again.")
        return
    
    print("Registration successful!")
    print("You have been successfully logged in.")

    return register_account()

register_account()
