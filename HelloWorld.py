def rangeFunction():
    for b in range(3,6):
        for x in range(2,b):
                if b % x == 0:
                        print(b, 'equals', x, '*', b//x)
                        break
        else:
                print(b, 'is prime')

def continueStatement():
    for num in range(2, 10):
        if num % 2 == 0:
            print('Even number', num)
            continue
        print('Odd number', num)

def passStatement():
    while True:
        pass #Busy-wait for keyboard interrupt (CTRL+C)

class AnEmptyClass:
    pass

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def main():
    fib(10)
    #passStatement()
    #rangeFunction()
    #continueStatement()


if __name__ == "__main__":
    main()