#  Taking n as input, print pyramid with n number of rows 

#  Input : 4
#  Output :
#         *
#       * * *
#     * * * * *
#   * * * * * * *

n = int(input("n = "))

for i in range(1, n+1):
    for j in range(1, n-i+1):
        print(" ", end = " ")

    for k in range(1, 2*i):
        print("*", end = " ")

    print()