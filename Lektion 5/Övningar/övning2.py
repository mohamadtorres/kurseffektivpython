print("*"*20)
#===================
# Skapa tv˚a olika generatorer: en som genererar tal och en som genererar deras
# kvadrater. Skriv en ny generator som kombinerar de tv˚a och returnerar tuple
# (tal, kvadrat).

def tal_generator(n):
    for _ in range(n):
        yield _

# tal_list = tal_generator(10)
# for num in tal_list:
#     print(num)
#bygger en lista
print("*" * 25)

#måste hämta tal_list en gång till annars det är förbrukad
# tal_list = tal_generator(10)
def kvadrat_generator(lista):
    for x in lista:
        yield x * x

# kvadrat_lista = kvadrat_generator(tal_list)
# for nummer in kvadrat_lista:
#     print(nummer)

print("*" * 25)

def tupple_generator(lista1,lista2):
    # indexering = 0
    # for lista1[indexering] in lista1:
    #     for lista2[indexering] in lista2:
    #         yield (lista1[indexering], lista2[indexering])
    #         indexering += 1
    #man gör inte så i generatorer att göra en för loop
    for item1, item2 in zip(lista1,lista2):
        yield (item1,item2)


tal_list = tal_generator(10)
kvadrat_lista = kvadrat_generator(tal_list)
tal_list = tal_generator(10)
tupple_lista = tupple_generator(tal_list,kvadrat_lista)


tal_list = tal_generator(10)
kvadrat_lista = kvadrat_generator(tal_list)
#Förklaring av problemet:

#När du först använder tal_list för att skapa kvadrat_lista med kvadrat_generator,
#konsumeras tal_list delvis. När du sedan använder den igen i tupple_generator, fortsätter den från där den slutade, vilket resulterar i varannan tuple i output.
tal_list = tal_generator(10)

tupple_lista = tupple_generator(tal_list,kvadrat_lista)
for i in tupple_lista:
    print(i)

# def tupple_generator(lista1, lista2):
#     for item1, item2 in zip(lista1, lista2):
#         yield (item1, item2)

# def tal_generator(n):
#     for i in range(n):
#         yield i

# def kvadrat_generator(talgen):
#     for tal in talgen:
#         yield tal ** 2

# # Skapa generatorer
# tal_list = tal_generator(10)
# kvadrat_lista = kvadrat_generator(tal_list)
# tupple_lista = tupple_generator(tal_list, kvadrat_lista)

# # Eftersom tal_list har förbrukats i kvadrat_generator, måste vi skapa om det
# tal_list = tal_generator(10)
# kvadrat_lista = kvadrat_generator(tal_list)
# tupple_lista = tupple_generator(tal_list, kvadrat_lista)

# for i in tupple_lista:
#     print(i)
