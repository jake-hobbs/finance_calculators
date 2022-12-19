'''
Import Math
Ask user to select which type of calculator they want to use
Depending on selection, ask for more details
If investment and simple interest
    print total
Elif investment and compound interest
    print total
Elif bond
    print monthly repayment
'''

# Import math

import math

# Ask user to select which type of calculator they want to use

print('''Choose either 'investment' or 'bond' from the menu below to proceed:

investment   -   to calculate the amount of interest you'll earn on your investment
bond         -   to calculate the amount you'll have to pay on a home loan\n''')

calculator_selection = input()


# Depending on selection, ask for more details 

if calculator_selection.upper() == "INVESTMENT":
    deposit = int(input("How much money are you depositing? "))
    interest_rate = float(input("What is the interest rate %? ")) / 100
    years = int(input("How many years do you plan on investing? "))
    interest = input("Do you want 'simple' or 'compound' interest? ")

elif calculator_selection.upper() == "BOND":
    house_value = int(input("What is the present value of the house? "))
    interest_rate = float(input("What is the interest rate %? ")) / 100
    months = int(input("How many months do you plan to take to repay the bond? "))

else:
    print("You haven't selected a valid type.")



# If investment and simple interest

if calculator_selection.upper() == "INVESTMENT" and interest.upper() == "SIMPLE":
    total_return = deposit * ((1 + interest_rate * years))
    print(f"Total Return: {round(total_return, 2)}   Interest included: {round((total_return - deposit),2)}")

# Elif invesment and compound interest

elif calculator_selection.upper() == "INVESTMENT" and interest.upper() == "COMPOUND":
    total_return = deposit * (math.pow((1 + interest_rate), years))
    print(f"Total Return: {round(total_return, 2)}   Interest included: {round((total_return - deposit),2)}")

# Elif bond

elif calculator_selection.upper() == "BOND":
    monthly_interest_rate = interest_rate / 12
    monthly_repayment = (monthly_interest_rate * house_value) / (1 - (1 + monthly_interest_rate) ** (- months))
    print(f"Your monthly bond repayment is: {round(monthly_repayment,2)}")

# Else an invalid selected

else:
    print("You haven't selected a valid type.")

