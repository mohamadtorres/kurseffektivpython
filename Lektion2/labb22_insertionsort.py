spelare = ["Ronaldo", "Messi", "De Bruyne", "Zlatan", "Kaka", "Zidane", "Neymar", "Buffon", "Bale", "Totti"]



def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        key = lista[i]
        j = i -1
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j = j -1
        lista[j+1] = key

    return lista


insert1 = insertion_sort(spelare)

print(insert1)
