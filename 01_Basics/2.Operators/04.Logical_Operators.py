# Logical Operators --> and(.), or(+), not

# and (True, when all the conditions are true)
print((5>2) and (5>3))                      # Both are true,        hence "True"
print((5>2) and (5<3))                      # I - true, II - false, hence "False"
print((5<2) and (5>9))                      # Both are false,       hence "False"

# or (True, when either of the condition is true)
#    (False, when all the conditions are false)
print((5>2) or (5>3))                      # Both are true,        hence "True"
print((5>2) or (5<3))                      # I - true, II - false, hence "True"
print((5<2) or (5>9))                      # Both are false,       hence "False"

# not (True  --> False)
#     (False --> True)
print(not(5>2))                            # Statement is True,  but Output will be "False"
print(not(5<2))                            # Statement is False, but Output will be "True"
print(not(5==2))                           # Statement is False, but Output will be "True"