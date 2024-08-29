GLOBAL_LISTA = [1,2,3,4]

def ytre_func():
    x = 5
    #mikhaim ye element az GLOBAL LISTA ro taghir bedim bebinim chejuri mishe
    GLOBAL_LISTA[0] = 6
    def inre_func():
        nonlocal x
        GLOBAL_LISTA[3]= 10
        x = 10
    print(x)
    inre_func()
    print(x)


ytre_func()
print(GLOBAL_LISTA)


def main():
    GLOBAL_LISTA = ["a", "b", "c"]
    print(GLOBAL_LISTA)
    ytre_func()

if __name__ == '__main__':
    main()