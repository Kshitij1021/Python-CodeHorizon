# Print "Low"  if marks <= 30
#       "Avg"  if 30 < marks < 70 
#       "High" if marks >= 70
# without using elif

marks = int(input("Enter your Marks: "))

if(marks < 70):
    if(marks <= 30):
        print("Low")
    else:
        print("Avg")

else:
    print("High")
