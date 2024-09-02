#Skapa ett set av alla vokaler som finns i str¨angen "comprehensions"
sträng = "comprehensions"
vokaler = ["a", "e", "y", "o", "i", "u", "ä","å","ö"]

ny_set = { vokal for vokal in vokaler if vokal in sträng}
print(ny_set)