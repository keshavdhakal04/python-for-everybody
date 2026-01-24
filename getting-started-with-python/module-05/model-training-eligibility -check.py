# A company only allows model training if:
# - Dataset size is greater than or equal to 10,000 records
# - Available RAM is at least 8 GB
#
# Ask the user to enter dataset size and RAM.
# Use try and except to handle invalid input.
#
# If both conditions are met, print:
# "Training can start"
# Otherwise, print:
# "Insufficient resources"

try : 
    datasetSize = int(input("Enter size of dataset : ")) #program will only crash while input
    ram = int(input("Enter RAM available (in GB) : "))

except:
    print("Invalid input, Must be an interger")

else: # if user enters an invalid input (like string/text), the variable (datasetSize and ram) will never be created.. 
    if datasetSize >= 10000 and ram >= 8:
        print("Training can start!!")
    else:
        print("Insufficient resources")