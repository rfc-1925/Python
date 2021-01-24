class ThisDict():
    phoneExtension = {'Cisco': 1234, 'Pete': 4321, 'Ge': 9999}

def main():
    person = input('Lookup user extension: ')
    #if ThisDict.phoneExtension[person]:
    print(ThisDict.phoneExtension[person])

if __name__ == "__main__":
    main()