# https://neetcode.io/problems/python-what-are-objects
# WAaaaaaaaaay too easy
#

class Pet:
    def __init__(self, name: str, species: str, hunger: int, energy: int):
        self.name = name
        self.species = species
        self.hunger = hunger
        self.energy = energy

# Don't modify the above code


whiskers = Pet("Whiskers", "cat", 6, 8)

# Don't modify the following code
print(f"{whiskers.name} ({whiskers.species}) - Hunger: {whiskers.hunger}, Energy: {whiskers.energy}") 
