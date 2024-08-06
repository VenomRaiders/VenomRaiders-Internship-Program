correct_username = "SAMTECH"
correct_password = "SAM123"

for attempt in range(3):
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == correct_username and password == correct_password:
        print("Login successful!")
        break
    else:
        print("Incorrect username or password.")

