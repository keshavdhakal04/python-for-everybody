# Ask the user to enter model accuracy (0–100).
# Use try and except to handle non-numeric input.
#
# If accuracy is:
# 90 or above → print "Production Ready"
# 75–89 → print "Needs Improvement"
# Below 75 → print "Reject Model"
#
# If the accuracy is outside 0–100, print "Invalid accuracy"

try:
    modelAccuracy = int(input("Enter model accuracy (0-100) : "))

    if modelAccuracy < 0 or modelAccuracy > 100: # runs if condition1 is true OR condition2 is true
        print("Out of range")
    elif modelAccuracy >= 90:
        print("Production Ready")
    elif modelAccuracy >= 75:
        print("Need Improvement")
    else:
        print("Reject Model")

except: 
    print("INVALID INPUT, MUST BE INTERGER")