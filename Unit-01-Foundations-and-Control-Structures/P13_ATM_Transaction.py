account_balance = 1000
withdrawal_amount = int(input("Enter the amount to withdraw: "))
pin = int(input("Enter your 4-digit PIN: "))

if pin == 1234:
    if withdrawal_amount <= account_balance:
        account_balance -= withdrawal_amount
        print("Withdrawal successful. Remaining balance: ", account_balance)
    else:
        print("Insufficient funds.")
else:
    print("Incorrect PIN.")
    