def summation(num):
    if num == 1:
        return 1

    return num + summation(num - 1)


while True:
    n = int(input("Enter a number: "))
    if n == -1:
        break
    print(summation(n))
