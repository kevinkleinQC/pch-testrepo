# Note that when running this script, nothing seemingly out of the ordinary happens.
# Yet, when feeding it to mypy...

from typing import Optional


class Person:
    def __init__(self, name: str, height_in_cm: int, favorite_tea: str = None):
        self.name = name
        self.height_in_cm = height_in_cm
        self.favorite_tea = favorite_tea


bob = Person("Bob", 172.5)

from typing import Optional

def get_age(person: str) -> Optional[int]:
    if person == "Bob":
        return 72
    if person == "Anne":
        return 27
    return None


print(get_age(bob))

from typing import Union


def pretty_print(string_or_int: Union[str, int]):
    print(f"*** {string_or_int} ***")


print(get_age(bob.name) * 7)

pretty_print(get_age(bob.name))

pretty_print(bob.favorite_tea)
