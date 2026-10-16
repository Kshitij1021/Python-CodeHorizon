#  Taking n as input, print a number spiral with n as its center

#  Input : 4
#  Output :
#   1 1 1 1 1 1 1
#   1 2 2 2 2 2 1
#   1 2 3 3 3 2 1
#   1 2 3 4 3 2 1
#   1 2 3 3 3 2 1
#   1 2 2 2 2 2 1
#   1 1 1 1 1 1 1

n = int(input("n = "))

for i in range(1, n+1):
    for j in range(1, n+1):
        print(min(i, j), end = " ")

    for k in range(n-1, 0, -1):
        print(min(i, k), end = " ")

    print()

for i in range(n-1, 0, -1):
    for j in range(1, n+1):
        print(min(i, j), end = " ")

    for k in range(n-1, 0, -1):
        print(min(i, k), end = " ")

    print()

