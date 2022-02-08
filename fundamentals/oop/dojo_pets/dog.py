
from pet import Pet

class Dog(Pet):
    def __init__(self, name, tricks, breed):
        super().__init__(name, "dog", tricks)
        self.breed = breed
    def noise(self):
        print("Bark Bark Bark")