class Animal:
    def __init__(self):
        # Initialise la classe avec deux attributs, age et nomanimal
        self.age = 0
        self.nomanimal = ""

    def vieillir(self):
        # Méthode qui incrémente l'âge de l'animal de 1
        self.age += 1

    def nommer(self, nom):
        # Méthode qui attribue un nom à l'animal
        self.nomanimal = nom

# Crée une instance de la classe Animal
animal = Animal()

# Affiche l'âge initial de l'animal
print("Âge initial de l'animal :", animal.age)

# Appelle la méthode vieillir pour augmenter l'âge de l'animal
animal.vieillir()
print("L'âge de l'animal après un an :", animal.age)

# Appelle la méthode nommer pour donner un nom à l'animal
animal.nommer("Brutus")
print("L'animal se nomme :", animal.nomanimal)