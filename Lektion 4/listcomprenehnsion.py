#lista med alla tal mellan 10 och 100
new_list = [x for x in range(10,101,10)]
print(new_list)

#lista med alla tal * 100 mellan 10 och 100
new_list1 = [x * 100 for x in range(10,101,10)]
print(new_list1)


stefan = "Stefan"
vokaler = "aouiyeäöå"

new_list2 = [ x for x in stefan if x in vokaler]

print(new_list2)