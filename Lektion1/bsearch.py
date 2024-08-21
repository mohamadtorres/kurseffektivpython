l = [1,2,2,4,8,12,13,14,17,19,21,22,33,43,44]


def binary_search(target:int, lista:list[int]) -> bool:
    start = 0
    end = len(lista) - 1

    
    while start <= end:
        mid = (end - start) // 2 #vill ha en int NOT follow
        if lista[mid] == target:
            return True
        elif lista [mid] < target:
            start = mid + 1

        else:
            start = mid - 1
    return False

while True:
    bs = int(input("Sök siffra: "))

    if binary_search(bs,l):
        print("hittat!")

    else:
        print("Finns ej!")

