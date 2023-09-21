def Fibonacci(num):
    if num <= 1:
        return num

    return Fibonacci(num - 1) + Fibonacci(num - 2)


while True:
    n = int(input("Enter number: "))
    if n == -1:
        break

    print(Fibonacci(n))
