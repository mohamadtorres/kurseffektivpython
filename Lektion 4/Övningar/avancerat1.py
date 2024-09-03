# Primtal och kvadrater: Skapa en lista med kvadrater av alla primtal
# mellan 1 och 50
from sympy import isprime
nylista = [ num ** 2 for num in range(1,51) if isprime(num) ]
print(nylista)


#=====================
# Anagram: Givet en lista med ord ["evil", "vile", "veil", "live"],
# skapa en dictionary d¨ar nycklarna ¨ar sorterade bokst¨aver av orden och
# v¨ardena ¨ar listor med ord som ¨ar anagram av varandra
nylista1 = ["evil", "vile", "veil", "live"]

nydict = {''.join(sorted(ord)):nylista1 for ord in nylista1}
print(nydict)


#=========================================
# N-gram frekvens: Givet en textstr¨ang, skapa en dictionary d¨ar nyck-
# larna ¨ar alla m¨ojliga par av bokst¨aver (bi-gram) och v¨ardena ¨ar antalet
# g˚anger varje par f¨orekommer i str¨angen.
sträng = "Mohammad Khavari dele mano bordi"
# Ta bort mellanrum
ren_sträng = sträng.replace(" ", "")
nydict1 = {ren_sträng[i:i+2]:ren_sträng.count(ren_sträng[i:i+2]) for i in range(len(ren_sträng))}
# par = list(itertools.combinations(sträng.replace(" ",""), 2))
# for p in par:
#     print(p)
print(nydict1)
