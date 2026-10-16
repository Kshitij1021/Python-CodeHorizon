#  Taking n as input, print a rhombus with n number of rows 

#  Input : 5
#  Output :
#           * * * * *
#         * * * * *
#       * * * * *
#     * * * * *
#   * * * * * 

n = int(input("n = "))

for i in range(1, n+1):
    for j in range(1, n-i+1):
        print(" ", end = " ")

    for k in range(1, n+1):
        print("*", end = " ")

    print()