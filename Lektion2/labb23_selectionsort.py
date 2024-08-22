spelare = ["Ronaldo", "Messi", "De Bruyne", "Zlatan", "Kaka", "Zidane", "Neymar", "Buffon", "Bale", "Totti"]


def insertion_sort(lista):
    n = len(lista)
    for i in range(n):
        minsta_index = i #vi TROR att den är den minsta
        for j in range(i+1, n): # sen jämför vi med resten
            if lista[j] < lista[i]:
                minsta_index = j #om nästa var större och vi hade trott fel då byter vi plats
        lista[i],lista[minsta_index] = lista[minsta_index],lista[i]

    return lista

insertion_sort_sorted = insertion_sort(spelare)
print(insertion_sort_sorted)

#Fati