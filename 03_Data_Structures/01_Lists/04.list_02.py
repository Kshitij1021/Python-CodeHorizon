# Write a code to print the average of all elements present in a list
marks = [60, 70, 80, 90]

sum = 0

for ele in marks:
    sum += ele

avg = sum / len(marks)
print(avg)