from car import Car
from timeit import default_timer
import string 
import random

ALPHABET = list(string.ascii_uppercase)
#stora bokstäver === ändra inte sen låt det vara för fan
DIGITS = list(string.digits)

def create_all_cars_with_all_licence_plates() -> list:
    d = {}
    for first_pos in ALPHABET:
        for second_pos in ALPHABET:
            for third_pos in ALPHABET:
                for i in DIGITS:
                    for j in DIGITS:
                        for k in DIGITS:
                            regnr = first_pos + second_pos + third_pos + i + j +k
                            d[ regnr] = Car(regnr, '', '')
    return d




def get_car_by_regno(regnr:str, list_of_cars:list[Car]):
    for car in list_of_cars:
        if car.regnr == regnr:
            return car
        
    return None


def main():
    t_start = default_timer()
    cars = create_all_cars_with_all_licence_plates()
    t_end = default_timer()
    random.shuffle(cars)

    print(f"Det tog {t_end - t_start} sekunder att spara alla bilar")
    

    while True:
        regnr = input ("Ange Regnr: ")


        if regnr == "q":
            break

        t_start = default_timer()
        t_end = default_timer()
        print(f"Sökningen tog {t_end - t_start} sekunder")

        car = get_car_by_regno(regnr, cars)
        if car :
            print("Hitta bil!")
        else:
            print("Bil finns inte")

if __name__ == '__main__':
    main()
