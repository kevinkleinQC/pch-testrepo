from Typing import Optional

class Person:
    def __init__(self, name: str, height_in_cm: int, favorite_tea: str = None):
        self.name = name
        self.height_in_cm = height_in_cm
        self.favorite_tea = favorite_tea

bob = Person("Bob", 172.5)

def get_age(person: str) -> Optional[int]:
    if person == "Bob":
      return 72
    if person == "Anne":
      return 27
    return None

print(get_age(bob))

def pretty_print(simple_string: str):
     print(f"*** {simple_string} ***")

pretty_print(get_age(bob))

pretty_print(bob.favorite_tea)
