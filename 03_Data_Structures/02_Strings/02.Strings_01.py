# Print the given string in reversed order

st = "Programming"
n = len(st)

for i in range(n):
    print(st[n-i-1], end = "")

# Alterate by string slicing
# print(st[ : :-1])
