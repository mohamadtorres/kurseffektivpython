# Gemensamma multiplar: Givet tv˚a set med tal {3, 6, 9, 12, 15,
# 18, 21, 24} och {4, 8, 12, 16, 20, 24}, skapa ett set med alla
# gemensamma multiplar.

set1 = {3, 6, 9, 12, 15, 18, 21, 24}
set2 = {4, 8, 12, 16, 20, 24}

nyset = {num for num in set1 if num in set2}
print(nyset)


#================

# Palindrom ord: Skapa ett set med alla ord fr˚an listan ["level",
# "radar", "world", "python", "civic", "rotor"] som ¨ar palindromer
# (ord som ¨ar samma framl¨anges och bakl¨anges).

listan = ["level","radar", "world", "python", "civic", "rotor"]
palindromset = {ord for ord in listan if ord[::-1] == ord}
print(palindromset)


#==================

