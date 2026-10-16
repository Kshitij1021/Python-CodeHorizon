# keep asking the passsword until the correct one is entered

Pass = "CodeHorizon"
n = input("Enter your password: ")
while(Pass != n):
    print("Your Password is wrong!")
    n = input("Enter your password: ")

print("The entered password is correct... Thank You!")