
APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name=None, breed=None):
        self.name=name
        self.breed=breed
    def get_name(self):
        print("Retrieving the name of the dog.")
        return self._name
    def set_name(self, name):
        if name is None:
            self._name=name
        elif (type(name) == str) and (1 <= len(name) <= 25):
            print(f"Setting the name of the dog to {name}")
            self._name=name
        else:
            print("Name must be string between 1 and 25 characters.")
    def get_breed(self):
        print("Retrieving the breed of the dog.")
        return self._breed
    def set_breed(self, breed):
        if breed is None:
            self._breed=None
        elif breed not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
        else:
            print(f"Setting the breed of the dog to {breed}")
            self._breed=breed
    name=property(get_name, set_name)
    breed=property(get_breed, set_breed)

