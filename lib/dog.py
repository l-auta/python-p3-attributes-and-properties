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
    def __init__(self, name = "None", breed = "Unknown"):
        self.name = name
        self.breed = breed

    def _get_name(self):
        return self._name

    def _test_name_under_25(self, value):
         if not isinstance(value, str) :
            print("Name must be string between 1 and 25 characters.")
         elif len(value) == 0 :
             print("Name must be string between 1 and 25 characters.")
         elif len(value) > 25 :
             print("Name must be string between 1 and 25 characters.")
         else:
            self._name = value 

    name = property(_get_name , _test_name_under_25)


    @property
    def breed(self):
        return self._breed 

    @breed.setter
    def breed(self, value):
         if value not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
         else:
            self._breed = value 

   
dog1 = Dog("" , "corgi")
