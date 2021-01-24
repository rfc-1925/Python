class AClass:
    aTuple = (1234, 9876, 'string')

def main():
    #print(AClass.aTuple)

    #print('\nNext show Turbles can be nested:')
    #anotherTuple = AClass.aTuple, (1,2,3,4,5)
    #print(anotherTuple)

    #print('\nNext show Turbles can contain mutable objects:')
    #v = ([1, 2, 3], [9, 8, 7])
    #print(v)

    #print('\nNext show Turbles are immutable:')
    #thirdTuple = AClass.aTuple[0] = 8888
    #print(thirdTuple)

    empty = ()
    singleton = 'test',
    #NOTICE THE COMMA ^
    print(len(empty))
    print(len(singleton))

if __name__ == "__main__":
    main()