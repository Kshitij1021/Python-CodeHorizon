#  Taking n as input, print a Bridge with n number of rows 

#  Input : 5
#  Output :
#   * * * * * * * * *
#   * * * *   * * * *
#   * * *       * * *
#   * *           * *
#   *               *

n = int(input("n = "))

for i in range(1, n+1):
    for j in range(1, 2*n):
        if((j <= (n-i+1)) or (j >= (n+i-1))):
           print("*", end = " ")

        else:
            print(" ", end = " ")

    print()
        