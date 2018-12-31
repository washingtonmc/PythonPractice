def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)


def main():
    number = int(input("Enter in a positive number:  "))
    print(str(number), " factorial is ", str(fact(number)))


if __name__ == '__main__':
    main()
