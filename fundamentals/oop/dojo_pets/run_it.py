
from pet import Pet
from ninja import Ninja
from dog import Dog

nacho = Pet("Nacho", "hedgehog", ["bite", "poop"])
n1 = Ninja("Tommy", "Rocha", "Cat Treats: Pizza Flavor", "Cat Food", nacho)

rue = Dog("Rue", ["Sit"], "Terrier")
n2 = Ninja("Ari", "Rosales", "Bacon Bites", "Rachel Ray's Dog Food", rue)


n1.feed().walk().bathe()
print("Nacho's Health", nacho.health)
print("Nacho's Energy", nacho.energy)
print()

n2.feed().walk().bathe()
print("Rue's Health", rue.health)
print("Rue's Energy", rue.energy)