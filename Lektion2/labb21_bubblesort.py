spelare = ["Ronaldo", "Messi", "De Bruyne", "Zlatan", "Kaka", "Zidane", "Neymar", "Buffon", "Bale", "Totti"]


# def bubble_sort(lista):
#     n = len(lista)
#     for i in range(n):
#         for j in range(n-i-1):#(n-i-1) för att with each complete pass in the list, the largest element of the unsorted is placed in its correct place and we dont need to look at older ones again
#             if lista[j] > lista[j+1]:
#                 lista[j], lista[j+1] = lista[j+1], lista[j]

#     return lista


def bubble_sort(lista):
    n = len(lista)
    for _ in range(n):
        for i in range(n-1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]

    return lista

sorterade_bubblesort = bubble_sort(spelare)
print(sorterade_bubblesort)