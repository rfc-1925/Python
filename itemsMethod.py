class itemsMethod():
    cars = {'Chevy': 'Camaro', 'Ford': 'Mustang'}
    for brand, model in cars.items():
        print('The brand is: ', brand, 'The model is: ', model)
def main():
    itemsMethod()

if __name__ == "__main__":
    main()