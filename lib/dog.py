#!/usr/bin/env python3

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
    def __init__(self, name = "sample", breed = "Pug"):
        self._name = None
        self._breed = None

        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds." )
        
        if self._breed is not None:
            self.name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            print(f"Setting name to { name }.")
            self._name = name

        else:
            print("Name must be string between 1 and 25 characters.")
            self._name = None

    def get_breed(self):
        return self._breed
    
    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            print(f"Setting breed to { breed }.")
            self._breed = breed

        else:
            print("Breed must be in list of approved breeds." )
            self._breed = None

    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)


