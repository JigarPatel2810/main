# # psudo code 
# 1. Create a file called control_flow_atm.py
# 2. Create a variable called balance with an int value representing the money in the
# user's account
# 3. Create a variable called pin with an int value (for example 1234)
# 4. Prompt the user to enter their pin !
# 5. If the pin values match, display their balance.
# 6. If they don't match, print out a message notifying the user.
# Extensions:
# 1. If the pin matches, give the prompt to the user if they'd like to withdraw or deposit
# some money.
# 2. Once they made their choice, prompt them to enter an amount.
# 3. Subtract or add the value to their account balance, then display the updated balance!

balance = int(5000)
pin = int(1234)
user_pin = int(input("enter the 4 digit pin:"))
if user_pin==pin:
    print(balance)
    user_input= input("enter deposite or withdraw: ")
    if user_input == "deposite":
        user_amount=int(input("enter amount to deposite:"))
        print(balance+user_amount)
    else :
         user_amount=int(input("enter amount to withdraw:"))
         print(balance-user_amount)
else:
        print("incorrect pin!")
