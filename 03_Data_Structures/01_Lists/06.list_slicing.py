# To access the list from any index

list =    [3, 5, 2, 7, 4, 10, 23, 21, 15, 12]
# Index -> 0  1  2  3  4   5   6   7   8   9

# [start, end, updation] --> Like range function

print(list[1:4])            # Indices --> 1, 2, 3
print(list[ :3])            # Indices --> 0, 1, 2
print(list[2: ])            # Indices --> 2, 3, ... 9
print(list[ : ])            # Indices --> 0, 1, ... 9
print(list[1:7:2])          # Indices --> 1, 3, 5
print(list[ : :2])          # Indices --> 0, 2, 4, 6, 8
print(list[1: :2])          # Indices --> 1, 3, 5, 7
