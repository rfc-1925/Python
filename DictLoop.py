def itemsMethod():
    cars = {'Chevy': 'Camaro', 'Ford': 'Mustang'}
    for brand, model in cars.items():
        print('The brand is: ', brand, 'The model is: ', model)

def enumerateMethod():
    for position, name in enumerate(['Cisco', 'Pete', 'Ge']):
        print (position, name)
        #show we can print in either order
        print (name, position)

def zipMethod():
    questions = ['a', 'b', 'c']
    answers = ['first', 'second', 'third']
    for q, a in zip(questions, answers):
        print('What position in the alphabet is {0}? It is the {1} letter.'.format(q, a))

def reversedMethod():
    for index in reversed(range(1, 10, 2)):
        print(index)

def sortedMethod():
    sandwhich = ['ham', 'cheese', 'letuce']
    for ingredient in sorted(sandwhich):
        print(ingredient)

def setMethod():
    sandwhich = ['ham', 'cheese', 'letuce']
    for ingredient in sorted(set(sandwhich)):
        print(ingredient)  

def main():
    #itemsMethod()
    #enumerateMethod()
    #zipMethod()
    #reversedMethod()
    #sortedMethod()
    setMethod()

if __name__ == "__main__":
    main()