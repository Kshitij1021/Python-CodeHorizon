def check(balance):
    print("Balance =", balance)

def deposit(a, balance):
    balance += a
    print("Balance =", balance)
    print("Deposited Successfully")

def withdraw(a, balance):
    balance -= a
    print("Balance =", balance)
    print("Withdrawed Successfully")


balance = 0
i = 1
while(i != 4):
    print("==========================ATM Simulator==========================")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    i = int(input("Enter the number corresponding to the operation to be executed: "))

    if(i == 1):
        print()
        print()
        print("Balance =", balance)

    elif(i == 2):
        a = int(input("Enter the amount to deposit: "))
        balance += a
        print("Balance =", balance)
        print("Deposited Successfully")

    elif(i == 3):
        a = int(input("Enter the amount to withdraw: "))
        if(a > balance):
            print()
            print()
            print("Insufficient Balance")
            continue
            print()
            print()
        else:
            balance -= a
            print("Balance =", balance)
            print("Withdrawed Successfully")

    elif(i == 4):
        break

    else:
        print("Enter a valid number")

    print()
    print()