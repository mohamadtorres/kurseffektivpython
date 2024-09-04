# Skapa en generator som genererar en o¨andlig sekvens av tal, men avslutas och
# kastar ett undantag n¨ar summan av alla genererade tal ¨overstiger ett visst v¨arde


def tal_generator(slutvärde):
    i = 0
    lista = 0
    while True:
        yield i
        lista += i
        i += 1
        if lista > slutvärde:
            raise ValueError("Summan av talen överstiger slutvärdet!")


nummer = tal_generator(50)

try:
    for num in nummer:
        print(num)
except ValueError as e:
    print(e)


print("*" * 25)

#==========================
# Skriv en generator som tar en str¨ang som indata och returnerar varje ord i
# str¨angen en i taget.
sträng = "mamad khavari dele mano bordi bordi delamo ino nakhordi"

def sträng_generator(sträng):
    nysträng = sträng.split()
    for ord in nysträng:
        yield ord

mesal = sträng_generator(sträng)
for _ in mesal:
    print(_)


print("*" * 25)
#===================
# Skriv en generator som tar en sekvens av tal och returnerar summan av alla tal
# upp till och med varje element i sekvensen. Exempel: f¨or sekvensen {1, 2, 3}
# b¨or generatorn returnera {1, 3, 6}
# print(range(5))

mamad = [1,2,3,4,5]
#rahe sakht
# def generator_mamad(lista):
#     for n in range(len(lista)):
#         if n == 0:
#             yield lista[0]
#         else:
#             i = lista[n]
#             for m in range(n):
#                 nylist= []
#                 nylist.append(lista[n-m])
#             yield i + sum(nylist)
            
def mamad_generatr(lista):
    summa = 0
    for num in lista:
        summa += num
        yield summa

mamadkhavari = mamad_generatr(mamad)
for number in mamadkhavari:
    print(number)
