# String Slicing
s = "Python Programming"
print(s[ :6])
print(s[ : ])
print(s[0: ])
print(s[0:6:2])


# String spliting
print(s.split(" "))                     # Wherever space is present, split the string
print(s.split("P"))                     # Wherever P is present, split the string
# After spiliting the string, the function saves each element in a list
s = "Python is a dynamic language"
a = s.split(" ")
print(a)

a = {1, 3, 4}
b = {3, 4}
print(a^b)