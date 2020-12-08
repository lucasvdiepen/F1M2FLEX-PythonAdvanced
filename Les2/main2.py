class BaseObject:
    sprite = None
    x = -1
    y = -1
    active = None

    def __init__(self, _x, _y, _active = True, _sprite = "een default sprite"):
        self.x = _x
        self.y = _y
        self.active = _active
        self.sprite = _sprite

    def PrintPosition(self):
        print("Object position x: " + str(self.x) + " y: " + str(self.y))

    def PrintObject(self):
        print("Dit object is een: ")

class Player(BaseObject):
    lives = 3
    speed = 5

    def __init__(self, _x, _y, _active = True, _sprite = "een player sprite"):
        super().__init__(_x, _y, _active, _sprite)

    def PrintPosition(self):
        print("Player position x: " + str(self.x) + " y: " + str(self.y))

    def PrintObject(self):
        super().PrintObject()
        print("Speler")

baseObject = BaseObject(20, 50) # Je hebt een instantie (instance/product) van ClassA gemaakt.

player = Player(200, 500) # Je hebt een instantie (instance/product) van ClassB gemaakt.

baseObject.PrintPosition() # De ClassA INSTANTIE roept een functie aan die in ClassB zou worden OVERSCHREVEN.

player.PrintPosition() # De ClassB INSTANTIE roept een functie aan die een functie uit ClassA OVERSCHRIJFT.

player.PrintObject() # De ClassB INSTANTIE roept een functie aan die VOORTBOUWT op een functie uit ClassA.

#Print sprite text
print(baseObject.sprite)

print(player.sprite)