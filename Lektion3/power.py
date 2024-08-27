from collections import abc


def generate_power_func(exponent:int) -> abc.Callable:
    def power(base):
        return base ** exponent
    return power

#exempel
to_the_power_of_4 = generate_power_func(4)
print(to_the_power_of_4)
#<function generate_power_func.<locals>.power at 0x0000021AF329AAC0>
#inja faghat behesh arg nadadim miad ye dune minne bara in funcion misaze
#dakhele khode function mibinim yue fun dige hast ke unam argument mikhad bara hamin chize khasi behemoon nemide

print(to_the_power_of_4(2))
#hala inja ye base ham midim bara func dakhele generate_power_func()
#javab hala mishe 16