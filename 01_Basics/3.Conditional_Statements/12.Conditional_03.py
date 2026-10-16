# Divisibility Check

# Write a Python program that takes an integer as input and checks its divisibility
# Display the appropriate message based on the following conditions:
# If the number is divisible by both 3 and 5, print:
# Divisible by both 3 and 5
# If the number is divisible only by 3, print:
# Divisible only by 3 
# If the number is divisible only by 5, print:
# Divisible only by 5 
# Otherwise, print:
# Not divisible by 3 or 5

num = int(input("n = "))

if((num % 15 == 0)):
    print("Divisible by both 3 and 5")
elif(num % 3 == 0):
    print("Divisible only by 3")
elif(num % 5 == 0):
    print("Divisible only by 5")
else:
    print("Not divisible by 3 or 5")