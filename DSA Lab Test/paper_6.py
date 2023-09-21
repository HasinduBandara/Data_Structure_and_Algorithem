def sumcube(num):
    if num == 1:
        return 1

    return num * num * num + sumcube(num - 1)


while True:
    n = int(input("Enter number: "))
    if n == -1:
        break

    print(sumcube(n))
