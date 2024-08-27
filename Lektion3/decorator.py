from faker import Faker

class Player:
    def __init__(self, name:str, age:int) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"Spelare {self.name} är {self.age} år gammal"

fake = Faker()

list_of_players = []

for _ in range (10000):
    list_of_players.append(Player(fake.name() , fake.random_int(min=15, max = 99)))



def get_oldest_player(list_of_players:list[Player]) -> Player:
    if not list_of_players:
        return None
    oldest = list_of_players[0]

    for player in list_of_players:
        if player.age > oldest.age:
            oldest = player

    return oldest
#doone doone una ro be tartibe sen michine o ma nafare aval ro migirim


def get_youngest_player(list_of_players:list[Player]) -> Player:
    if not list_of_players:
        return None
    youngest = list_of_players[0]

    for player in list_of_players:
        if player.age < youngest.age:
            youngest = player

    return youngest


print(get_oldest_player(list_of_players=list_of_players))
print(get_youngest_player(list_of_players=list_of_players))



def calculate_total_sum(*args):
    total_sum = 0
    for number in args:
        total_sum += number

    print(total_sum)