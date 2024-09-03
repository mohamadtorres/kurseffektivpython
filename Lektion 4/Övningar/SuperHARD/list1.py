# Pythagoreiska tripplar: Skapa en lista med alla pythagoreiska trip-
# plar (a, b, c) d¨ar a2 + b2 = c2 och 1 ≤ a, b, c ≤ 100. Varje trippel ska
# representeras som en tuple (a, b, c).

#pythogaros = a2 + b2 = c2

#FEL
#list1 = [(a,b,c) if 1 <= a and b and c <= 100 and a**2 + b**2 == c**2]
#print(list1)
#aval bayad dakehele hame itera konam
#inja mesle engelska zadam
#bayad baraye har a b ya c man gå genom konam

#RÄTT
list1 = [(a,b,c) for a in range(1,101) for b in range(1,101) for c in range(1,101) if a**2 + b**2 == c**2]
#print(list1)


#=============================
# Primosummor: Givet en lista med tal [2, 3, 5, 7, 11, 13, 17,
# 19, 23, 29], skapa en ny lista d¨ar varje element ¨ar summan av prim-
# talen upp till och med det primtalet.

primlista = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

nyprimlista = [sum(primlista[:x+1]) for x in range(len(primlista))]
print(nyprimlista)

#man ska använda range för att kunna komma till index. om man skriver inte range då går den till direkt x. INTE TILL INDEX X

#==============================

# Permutationslistor: Skapa en lista som inneh˚aller alla m¨ojliga per-
# mutationer av listan [1, 2, 3, 4]. Varje permutation ska represen-
# teras som en lista.
import itertools
listan = [1, 2, 3, 4]
permutationslista = [list(p) for p in itertools.permutations(listan)]
print(permutationslista)