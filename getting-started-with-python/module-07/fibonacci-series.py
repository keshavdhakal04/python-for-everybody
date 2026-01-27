#Display Fibonacci series

def fibonacciSeries(n):
    a = 0
    b = 1

    for i in range(n):
        print(a)
        c = a + b
        a = b
        b = c

num = int(input("Enter number to terms : "))
fibonacciSeries(num)