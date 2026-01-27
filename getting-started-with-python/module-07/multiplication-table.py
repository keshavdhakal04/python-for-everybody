#Print multiplication table of a given number

def Table(a):
    for i in range(1,11,1):
        #print(a," x ",i," = ", a*i)
        print(f"{a} x {i} = {a*i}")

num = int(input("Enter a number: "))
Table(num)
