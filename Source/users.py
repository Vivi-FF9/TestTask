from dataclasses import dataclass


@dataclass
class User:
    name: str
    customer_id: int


HarryPotter = User("Harry Potter", 2)
