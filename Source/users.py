from dataclasses import dataclass


@dataclass
class User:
    username: str
    customer_id: int


HarryPotter = User("Harry Potter", 2)
