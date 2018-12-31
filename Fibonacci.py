def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)


def main():
    number=int(input("Enter in a number greater than 0:  "))
    print(str(number), " Fibonacci number is ", str(fib(number)))


if __name__ == '__main__':
    main()
