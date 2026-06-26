# Print "Low"  if marks <= 30
#       "Avg"  if 30 < marks < 70 
#       "High" if marks >= 70
# using elif

marks = int(input("Enter your Marks: "))

if (marks<=30):
    print("Low")
elif ((marks>30) and (marks<70)):
    print("Avg")
else:
    print()