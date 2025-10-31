from animal import Animal


class Prey(Animal):
    def __init__(self, island, x=0, y=0, name="O", breed_n=2):
        Animal.__init__(self, island, x, y, name, breed_n)
