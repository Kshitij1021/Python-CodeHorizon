#   Taking number of rows as input, print the pascal triangle

#   n = 5 
#        1 
#       1 1
#      1 2 1
#     1 3 3 1
#    1 4 6 4 1
#   1 5 10 10 5 1 

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

def nCr(n, r):
    return ((factorial(n)) // ((factorial(r) * factorial(n-r))))

n = int(input("Enter number of rows: "))
for i in range(0, n+1):
    for j in range(2*(n-i)+1, 0, -2):
        print("", end=" ")

    for r in range(0, i+1):
        print(nCr(i, r), end=" ")

    print()
