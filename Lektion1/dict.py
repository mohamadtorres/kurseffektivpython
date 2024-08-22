from car import Car
from timeit import default_timer
import string 
import random
import os
import sys

ALPHABET = list(string.ascii_uppercase)
#stora bokstäver === ändra inte sen låt det vara för fan
DIGITS = list(string.digits)

def create_all_cars_with_all_licence_plates() -> dict:
    d = {}
    for first_pos in ALPHABET:
        for second_pos in ALPHABET:
            for third_pos in ALPHABET:
                for i in DIGITS:
                    for j in DIGITS:
                        for k in DIGITS:
                            regnr = first_pos + second_pos + third_pos + i + j +k
                            d[regnr] = Car(regnr, '', '')
    return d




def get_car_by_regno(regnr:str, dict_of_cars:dict[str:Car]):
    if regnr in dict_of_cars:
        return dict_of_cars[regnr]
        
    return None

 
def main():
    t_start = default_timer()
    cars_dict = create_all_cars_with_all_licence_plates()
    t_end = default_timer()
    # random.shuffle(cars_list)

    print(f"Det tog {t_end - t_start:.2f} sekunder att spara alla bilar och tar upp {sys.getsizeof(cars_dict)//10**6:.2f} Mb")
    

    while True:
        regnr = input ("Ange Regnr: ")


        if regnr == "q":
            break

        t_start = default_timer()
        t_end = default_timer()
        print(f"Sökningen tog {t_end - t_start:.2f} sekunder")

        car = get_car_by_regno(regnr, cars_dict)
        if car :
            print("Hitta bil!")
        else:
            print("Bil finns inte")

if __name__ == '__main__':
    main()
