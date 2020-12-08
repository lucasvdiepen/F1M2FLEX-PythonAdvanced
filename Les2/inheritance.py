class Character:
    speed = 10
    points = 0
    sprite = None

    def __init__(self):
        print("De constructor van Character")

    def Walk(self):
        print("Character loopt nu met snelheid", self.speed)



class Mario(Character):
    lives = 3
    item = None

    def __init__(self):

        super().__init__()

        self.speed = 30

    def Jump(self):
        print("Mario springt!")



characterA = Character()
marioX = Mario()

characterA.Walk()
marioX.Walk()

print(characterA.speed)
print(marioX.speed)
print(marioX.lives)

print(marioX)