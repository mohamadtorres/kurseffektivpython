from dataclasses import dataclass, field
from typing import List


#Gammalt sätt att fixa class
# class Human:
#     def __init__(self, name:str, age:int, occupation:str) -> None:
#         self.name = name
#         self.age = age
#         self.occupation = occupation

#     def __repr__(self) -> str:
#         return f"{self.name}"


# human1 = Human()
# human2 = Human()


#dataclass är ett sätt att korta ner kodet

#en annan model och sätt att bygga en class
@dataclass
class Human:
    name: str
    age: int
    occupation: str



@dataclass
class Grade:
    subject: str
    grade: int


@dataclass
class Student:
    name: str
    age: int
    grades: list[int] = field(default_factory=list)
    id: int = field(default=0, compare=False)
                    

    def average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0.0

class StupidClass:
    def __init__(self, dum_lista:list=[]) -> None:
        self.lista = dum_lista


a = StupidClass()
b = StupidClass()


