#Enkel generator
#Skapa en generator som returnerar kvadraten av varje tal fr˚an 1 till 10.
print("*"*20)

def squarenumbers(n):
    for x in range(n+1):
        yield (x ** 2)


# nums
# = generators(11)
# print(nums)
#den visar bara platsen till objektet
#<generator object generators at 0x00000208DEFE98A0>

nums= squarenumbers(10)
for num in nums:
    print(num)



#===================
#Skriv en generator som genererar en o¨andlig sekvens av naturliga tal (1, 2, 3,. . . ). T¨ank p˚a hur du kan avsluta denna sekvens i ett program
def oändlig():
    x = 0
    while True:
        yield x 
        x += 1

nums1 = oändlig()
# for nummer in nums1:
#     print(nummer)


#==============
# Skapa en generator som genererar Fibonacci-sekvensen. Sekvensen b¨orjar med
# 0 och 1, och varje efterf¨oljande tal ¨ar summan av de tv˚a f¨oreg˚aende talen.
print("*"*20)


def fibonaci(n):
    # for x in range(1,n+1):
    #     if x ==1:
    #         yield 1
    #     elif x ==2:
    #         yield 2
    #     elif x > 2:
    #         yield fibonaci[x-2] + fibonaci[x-1]
#     Du försöker referera till tidigare genererade värden med fibonaci[x-2] och fibonaci[x-1], 
#     men det är inte hur generatorer eller funktioner fungerar i Python. Du kan inte indexera direkt in i en generatorfunktion på det sättet.
# Du behöver lagra de tidigare två talen i variabler och använda dessa för att beräkna nästa tal i sekvensen.
    a,b = 0,1
    for i in range(n):
        yield a
        a,b = b, a+b
mamad = fibonaci(5)
for num in mamad:
    print(num)
    
    #==========================

# Skriv en generator som genererar alla primtal. Fundera p˚a hur du effektivt kan
# kontrollera om ett tal ¨ar ett primtal
print("*"*20)
from sympy import isprime

def primtal(n):
    for x in range(n):
        if isprime(x):
            yield x


primhast = primtal(10)
for num in primhast:
    print(num)



print("*"*20)
#======================
#Skapa en generator som tar en annan generator som indata och filtrerar ut alla
#j¨amna tal. Anv¨and en av dina tidigare generatorer som indata.

def jämnatal(lista):
    for x in lista:
        if x % 2 == 0:
            yield x

nums = squarenumbers(10)
#Förklaring:

#Generatorer: Generatorer är "engångsbruk" - när de väl har itererats genom en gång, 
# finns det inga fler värden att hämta från dem. I din ursprungliga kod blev nums förbrukad när den användes i jämnatal.
#Skapa en ny instans: Genom att skapa en ny instans av nums när du ska använda den,
#  kan du säkerställa att du itererar genom de värden som du förväntar dig.
jämnhast = jämnatal(nums)
for num in jämnhast:
    print(num)