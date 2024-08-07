# Step 1: You will make a bank account simulation where the user will enter their username and password
# If the username and password is not equal to the one stored in the fake database, tell the user they
# are unauthorized
# And exit(stop running)
# hint: for the fake database, you can simply use variables to store the username and the password before
# the program is
# run

#Here is an example

# [Hello there, welcome to my :Name: Bank, Enter your username and password to proceed
# Username: ________
# Password: ________
# On successful login, use this mesage: "Successfully Logged In"
# Print the current balance to the user

# Step 2: Provide the user with two options to either deposit or withdraw
# Sample message
# Which action do you want to carry out in your bank account(1. Withdraw 2. Deposit): ________
#

# Step 3: If it is withdrawal, ask the user to enter the amount they want to withdraw. If it is a deposit,
# ask the user
# the amount the wish to deposit. Print a message indicating that the deposit/withdrawal was successful.

# Step 4: Update the user with their new account balance


# Start of the program
# step 1
username = "hanslett"
password = "1234"

print("Hello there, Welcome to VenomRaiders Bank, Enter your username and password to proceed \n\n")
print("Enter your credentials")
usersname = input("Username: ")
userspassword = input("Password: ")

if usersname != username and password != userspassword:
    print("Sorry!, You are unauthorized")
    return ""
    
print("Sucessfully logged In")

# step 2
print("Which action do you want to carry out in your bank account?")
print("1. Deposit\n 2. Withdraw\n")
action = int(input("Choose an option: "))


# step 3
account_balance = 100_000

if action == 1:
    deposit = int(input("Enter the amount to be deposited: "))
    account_balance = account_balance + deposit
    print(str(deposit) + "XAF Deposited Sucessfully!")
elif action == 2:
    withdraw = int(input("Enter the amount to be withdrawn: "))
    account_balance = account_balance - withdraw
    print(str(withdraw) + "XAF Withdrawn Sucessfully!")

# step 4
print("New Account Balance: ", account_balance)
print("\nThank you for using VenomRaiders Bank services!!!")
