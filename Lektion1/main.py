from car import Car
from timeit import default_timer
import string 
import random
import os

ALPHABET = list(string.ascii_uppercase)
#string.ascii_uppercase genererar en lista av alla engelska bokstäver
#stora bokstäver === ändra inte sen låt det vara för fan
DIGITS = list(string.digits)

def create_all_cars_with_all_licence_plates() -> list:
    l = []
    for first_pos in ALPHABET:
        for second_pos in ALPHABET:
            for third_pos in ALPHABET:
                for i in DIGITS:
                    for j in DIGITS:
                        for k in DIGITS:
                            regnr = first_pos + second_pos + third_pos + i + j +k
                            l.append(Car(regnr, '', ''))
    return l

def get_car_by_regno(regnr:str, list_of_cars:list[Car]):
    for car in list_of_cars:
        if car.regnr == regnr:
            return car
        
    return None


def main():
    t_start = default_timer()
    cars = create_all_cars_with_all_licence_plates()
    t_end = default_timer()
    

    print(f"Det tog {t_end - t_start:.2f} sekunder att spara alla bilar")
    

    while True:
        regnr = input ("Ange Regnr: ")


        if regnr == "q": break

        car = get_car_by_regno(regnr, cars)
        if car :
            t_start = default_timer()
            t_end = default_timer()
            print(f"Sökningen tog {t_end - t_start:.2f} sekunder")
            print("Hitta bil!")
        else:
            print("Bil finns inte")

if __name__ == '__main__':
    main()
