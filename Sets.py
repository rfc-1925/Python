class MySet():
    #Creates an empty set named thisSet
    thisSet = ()
    print('This is an empty set', thisSet)

    #Creates a set with as an unordered collection of elements
    anotherSet = {'red', 'green', 'blue', 'purple'}
    print('The colors in this set are not in a specific index like a list ', anotherSet)

    #User input to check if the color exists within the set
    color = input('Enter in a color: ')

    #Check - print 'yes' if it exists otherwise print 'no'
    if color in anotherSet:
        print('yes')
    else:
        print('no')
    

def main():
    MySet()   

if __name__ == "__main__":
    main()
