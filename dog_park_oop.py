
class Dog:
    species = 'Canis familiaris'
    def __init__(self, name, age):
        self.name=name
        self.age = age
        # self.breed = breed

    def __str__(self):
        return f"{self.name} is {self.age} years old."

    def speak(self, sound):
        return f"{self.name} says {sound}"

class JackRusselTerrier(Dog):
    def speak(self, sound="Arf!"):
        return super().speak(sound)

class AustralianShepherd(Dog):
    pass

class Beagle(Dog):
    pass


if __name__=="__main__":
    miles = JackRusselTerrier('miles',4)
    print(miles)
    koffee = AustralianShepherd('koffee',5)
    print(koffee)
    print(koffee.speak("woof!"))
    print(miles.speak())
