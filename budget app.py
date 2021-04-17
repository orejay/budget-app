class Budget:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
    def Deposit(self):
        self.amount += depositamount
        print(f"you have #{category_one.amount} for food, #{category_two.amount} for clothing, #{category_three.amount} for home bills and #{category_four.amount} for other expenses")
    def Withdrawal(self):
        self.amount -= withdrawalamount
    def Transfer(self):
        self.amount += withdrawalamount
        print(f"you have #{category_one.amount} for food, #{category_two.amount} for clothing, #{category_three.amount} for home bills and #{category_four.amount} for other expenses")
category_one = Budget('Food', 25000)
category_two = Budget('Clothing', 20000)
category_three = Budget('Home bills',  35000)
category_four = Budget('Miscellaneous', 75000)
valid_options = [1,2,3,4]
action = int(input('Welcome ore, what would you like to do? \n 1) Withdraw 2) Deposit \n 3) Transfer 4) Check budget balances \n'))
while ( action not in valid_options):
    print('invalid option, please try again')
    action = int(input('Welcome ore, what would you like to do? \n 1) Withdraw 2) Deposit \n 3) Transfer 4) Check budget balances \n'))
if (action == 1):
    categoryW = int(input('what category would you like to Withdraw from? 1)Food  2)Clothing \n 3)Home_bills  4)Miscellaneous \n'))
    while ( categoryW not in valid_options):
        print('invalid option, please try again')
        categoryW = int(input('what category would you like to Withdraw from? 1)Food  2)Clothing \n 3)Home_bills  4)Miscellaneous \n'))
    if (categoryW == 1):
        withdrawalamount = int(input('How much would you like to withdraw from food? \n'))
        while ( withdrawalamount > category_one.amount):
            print('insufficient balance in budget category')
            withdrawalamount = int(input('How much would you like to withdraw from food? \n'))
        category_one.Withdrawal()
        print(f"you have #{category_one.amount} for food, #{category_two.amount} for clothing, #{category_three.amount} for home bills and #{category_four.amount} for other expenses")
    elif (categoryW == 2):
        withdrawalamount = int(input('How much would you like to withdraw from clothing? \n'))
        while ( withdrawalamount > category_two.amount):
            print('insufficient balance in budget category')
            withdrawalamount = int(input('How much would you like to withdraw from clothing? \n'))
        category_two.Withdrawal()
        print(f"you have #{category_one.amount} for food, #{category_two.amount} for clothing, #{category_three.amount} for home bills and #{category_four.amount} for other expenses")
    elif (categoryW == 3):
        withdrawalamount = int(input('How much would you like to withdraw from home bills? \n'))
        while ( withdrawalamount > category_three.amount):
            print('insufficient balance in budget category')
            withdrawalamount = int(input('How much would you like to withdraw from home bills? \n'))
        category_three.Withdrawal()
        print(f"you have #{category_one.amount} for food, #{category_two.amount} for clothing, #{category_three.amount} for home bills and #{category_four.amount} for other expenses")
    elif (categoryW == 4):
        withdrawalamount = int(input('How much would you like to withdraw from miscellaneous? \n'))
        while ( withdrawalamount > category_four.amount):
            print('insufficient balance in budget category')
            withdrawalamount = int(input('How much would you like to withdraw from miscellaneous? \n'))
        category_four.Withdrawal()
        print(f"you have #{category_one.amount} for food, #{category_two.amount} for clothing, #{category_three.amount} for home bills and #{category_four.amount} for other expenses")
elif (action == 2):
    categoryD = int(input('what category would you like to deposit into? 1)Food  2)Clothing \n 3)Home_bills  4)Miscellaneous \n'))
    while ( categoryD not in valid_options):
        print('invalid option, please try again')
        categoryD = int(input('what category would you like to deposit into? 1)Food  2)Clothing \n 3)Home_bills  4)Miscellaneous \n'))
    if (categoryD == 1):
        depositamount = int(input('How much would you like to deposit into food? \n'))
        category_one.Deposit()
    elif (categoryD == 2):
        depositamount = int(input('How much would you like to deposit into clothing? \n'))
        category_two.Deposit()
    elif (categoryD == 3):
        depositamount = int(input('How much would you like to deposit into home bills? \n'))
        category_three.Deposit()
    elif (categoryD == 4):
        depositamount = int(input('How much would you like to deposit into miscellaneous? \n'))
        category_four.Deposit()
elif (action == 3):
    transfer_origin = int(input('where would you like to transfer from?\n 1) Food 2) Clothing \n 3) Home bills 4) Miscellaneous \n'))
    while ( transfer_origin not in valid_options):
        print('invalid option, please try again')
        transfer_origin = int(input('where would you like to transfer from?\n 1) Food 2) Clothing \n 3) Home bills 4) Miscellaneous \n'))
    transfer_destination = int(input('where would you like to transfer into?\n 1) Food 2) Clothing \n 3) Home bills 4) Miscellaneous \n'))
    while ( transfer_destination not in valid_options):
        print('invalid option, please try again')
        transfer_destination = int(input('where would you like to transfer into?\n 1) Food 2) Clothing \n 3) Home bills 4) Miscellaneous \n'))
    if (transfer_origin == 1):
        withdrawalamount = int(input('How much would you like to transfer from food? \n'))
        while ( withdrawalamount > category_one.amount):
            print('insufficient balance in budget category')
            withdrawalamount = int(input('How much would you like to transfer from food? \n'))
        category_one.Withdrawal()
    elif (transfer_origin == 2):
        withdrawalamount = int(input('How much would you like to transfer from clothing? \n'))
        while ( withdrawalamount > category_two.amount):
            print('insufficient balance in budget category')
            withdrawalamount = int(input('How much would you like to transfer from clothing? \n'))
        category_two.Withdrawal()
    elif (transfer_origin == 3):
        withdrawalamount = int(input('How much would you like to withdraw from home bills? \n'))
        while ( withdrawalamount > category_three.amount):
            print('insufficient balance in budget category')
            withdrawalamount = int(input('How much would you like to withdraw from home bills? \n'))
        category_three.Withdrawal()
    elif (transfer_origin == 4):
        withdrawalamount = int(input('How much would you like to withdraw from miscellaneous? \n'))
        while ( withdrawalamount > category_four.amount):
            print('insufficient balance in budget category')
            withdrawalamount = int(input('How much would you like to withdraw from miscellaneous? \n'))
        category_four.Withdrawal()
    if (transfer_destination == 1):
        category_one.Transfer()
        if (transfer_origin == 1):
            print('NOTE: You just transferred from your food budget to your food budget!!!') 
        elif (transfer_origin == 2):
            print('You have successfully transferred from your clothing budget to your food budget')
        elif (transfer_origin == 3):
            print('You have successfully transferred from your home bills budget to your food budget')
        elif (transfer_origin == 4):
            print('You have successfully transferred from your miscellaneous budget to your food budget')
    elif (transfer_destination == 2):
        category_two.Transfer()
        if (transfer_origin == 1):
            print('You have successfully transferred from your food budget to your clothing budget') 
        elif (transfer_origin == 2):
            print('NOTE: You just transferred from your clothing budget to your clothing budget!!!')
        elif (transfer_origin == 3):
            print('You have successfully transferred from your home bills budget to your clothing budget')
        elif (transfer_origin == 4):
            print('You have successfully transferred from your miscellaneous budget to your clothing budget')
    elif (transfer_destination == 3):
        category_three.Transfer()
        if (transfer_origin == 1):
            print('You have successfully transferred from your food budget to your home bills budget') 
        elif (transfer_origin == 2):
            print('You have successfully transferred from your clothing budget to your home bills budget')
        elif (transfer_origin == 3):
            print('NOTE: You just transferred from your home bills budget to your home bills!!!')
        elif (transfer_origin == 4):
            print('You have successfully transferred from your miscellaneous budget to your home bills budget')
    elif (transfer_destination == 4):
        category_four.Transfer()
        if (transfer_origin == 1):
            print('You have successfully transferred from your food budget to your miscellaneous budget') 
        elif (transfer_origin == 2):
            print('You have successfully transferred from your clothing budget to your miscellaneous budget')
        elif (transfer_origin == 3):
            print('You have successfully transferred from your home bills budget to your miscellaneous budget')
        elif (transfer_origin == 4):
            print('NOTE: You just transferred from your miscellaneous budget to your miscellaneous!!!')
elif (action == 4):
    Balance_type = int(input('where would you like to transfer into?\n 1) Food 2) Clothing \n 3) Home bills 4) Miscellaneous \n'))
    while (Balance_type not in valid_options):
        print('invalid option, please try again')
        Balance_type = int(input('where would you like to transfer into?\n 1) Food 2) Clothing \n 3) Home bills 4) Miscellaneous \n'))
    if (Balance_type == 1):
        print(f" Your food budget is #{category_one.amount}")
    elif (Balance_type == 2):
        print(f" Your clothing budget is #{category_two.amount}")
    elif (Balance_type == 3):
        print(f" Your home bills budget is #{category_three.amount}")
    elif (Balance_type == 4):
        print(f" Your miscellaneous budget is #{category_four.amount}")
