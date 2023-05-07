from dataclasses import dataclass


@dataclass
class User:
    name: str
    user_id: int
    role: str = 'customer'


HermoineGranger = User("Hermoine Granger", 1)
HarryPotter = User("Harry Potter", 2)
RonWeasly = User("Ron Weasly", 3)
AlbusDumbledore = User("Albus Dumbledore", 4)
NevilleLongbottom = User("Neville Longbottom", 5)
