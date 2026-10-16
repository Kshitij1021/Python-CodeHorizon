#  Taking n as input, print a number zoom
#  Input : 4
#  Output :
#   1 1 1 1
#   1 2 2 2
#   1 2 3 3
#   1 2 3 4

n = int(input("n = "))

for i in range(1, n+1):
    for j in range(1, n+1):
        print(min(i, j), end = " ")

    print()