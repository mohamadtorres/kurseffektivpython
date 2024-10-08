from car import Car
import string
from timeit import default_timer

ALPHABET = list(string.ascii_uppercase)
#kommer ge dig ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

DIGITS = list(string.digits)
#kommer ge dig ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


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


def main():
    t_start = default_timer()
    cars = create_all_cars_with_all_licence_plates()
    t_end = default_timer()
    print(f"Det tog {t_end - t_start:.2f} sekunder att skapa listan")

if __name__ == '__main__':
    main()

