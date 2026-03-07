#simple pay calculator

#input 
name = input("Enter you name: ")
hoursWorked = input("How many hours did you work? : ")
ratePerHour = input("What's your hourly pay? : ")
                    
#process
pay = float(hoursWorked) * float(ratePerHour)

#output
print("\n--- Pay Summary ---")
print("Name:", name)
print("Hours Worked:", hoursWorked)
print("Hourly Rate:", ratePerHour)
print("Total Pay:", pay)