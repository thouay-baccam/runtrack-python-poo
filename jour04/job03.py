class Rectangle:

    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, largeur):
        self.__largeur = largeur

    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    def surface(self):
        return self.__longueur * self.__largeur

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    def get_hauteur(self):
        return self.__hauteur

    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur

    def volume(self):
        return self.surface() * self.__hauteur

rectangle1 = Rectangle(13, 34)
print("Perimètre du rectangle :", rectangle1.perimetre())
print("Surface du rectangle :", rectangle1.surface())

rectangle1.set_longueur(15)
rectangle1.set_largeur(36)
print("Perimètre du rectangle après la modif :", rectangle1.perimetre())
print("Surface du rectangle après la modif :", rectangle1.surface())

parallelepipede1 = Parallelepipede(6, 7, 8)
print("Volume du parallelepipede :", parallelepipede1.volume())
