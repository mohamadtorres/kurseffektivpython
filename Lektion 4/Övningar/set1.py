# Skapa ett set med kvadrater av alla unika tal i listan [1, 2, 2, 3, 4, 4, 5].


#rahe toolani khodam
listan = [1, 2, 2, 3, 4, 4, 5]
nylista = [num ** 2 for num in listan]
print(set(nylista))



#inja fahmidam hamin ke ba set neshon bedam khodesh set mishe niaz be kar dige nis
#hamin {} ke bezaram dore shartam yaeni ke javabesho set mikham
listan = [1, 2, 2, 3, 4, 4, 5]
ny_set = {num ** 2 for num in listan}

print(ny_set)