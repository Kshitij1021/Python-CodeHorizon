# Student Grade Calculator

# Assign grades based on marks.

# 90 and above --> Grade A
# 75 - 89 --> Grade B
# 60 - 74 --> Grade C
# 40 - 59 --> Grade D
# Below 40 --> Fail

num = int(input("Enter your marks: "))

if((num <= 100) and (num >= 90)):
    print("Grade A")
elif((num < 90) and (num >=75)):
    print("Grade B")
elif((num < 75) and (num >= 60)):
    print("Grade C")
elif((num < 60) and (num >= 40)):
    print("Grade D")
elif((num < 40) and (num >= 0)):
    print("Fail")
else:
    print("Enter valid marks")