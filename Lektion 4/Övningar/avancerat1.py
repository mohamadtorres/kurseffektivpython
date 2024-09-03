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

