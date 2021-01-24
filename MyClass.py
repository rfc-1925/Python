class MyClass:
    name = "Ge"
    food = "Burger"

def main():
    print(MyClass.name)
    print(MyClass.food)
    del(MyClass.food)
    print(MyClass.food)

if __name__ == "__main__":    
    main()