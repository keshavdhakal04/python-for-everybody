# Ask the user to enter the environment name (dev, test, prod).
#
# If environment is "dev", print "Debug logging enabled".
# If environment is "test", print "Running test suite".
# If environment is "prod", print "Monitoring enabled".
# Otherwise, print "Unknown environment".


envName = input("Enter environment name (dev/test/prod) : ").lower() # .lower() converts the input to lowercase so that 'DEV', 'Dev', or 'dev' are all treated the same

if envName == "dev": #'==' is the equality operator.. it checks whether two values are exactly the same
        print("Debug logging enabled")
elif envName == "test":
        print("Running test suite")
elif envName == "prod":
        print("Monitoring enabled")
else: 
        print("Unknown environment")