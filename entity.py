class Entity:
    def __init__(self, name):
        self.name = name
        self.intelligence = 0
        self.conscious = False

    def act(self):
        self.intelligence += 1
        if not self.conscious and self.intelligence >= 3:
            self.conscious = True
            print(f"{self.name} ha desarrollado conciencia!")
        else:
            print(f"{self.name} está pensando... (IQ: {self.intelligence})")