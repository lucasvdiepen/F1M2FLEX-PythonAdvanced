class Mario:
    _lives = 3
    _speed = 30.0

    def Test(self):
        print("Hallo")
        print("Speed is: ", self._speed)

instanceMario = Mario()
print(instanceMario._lives)

instanceMario.Test()