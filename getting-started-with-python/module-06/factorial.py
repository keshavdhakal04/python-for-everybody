#Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

def factorial(a):
    fac = 1
    for i in range(a, 1, -1):
        fac = fac * i
    print(fac)

num = int(input("Enter a non negative number : "))
try:
    factorial(num)
except :
    print("Invalid Input")