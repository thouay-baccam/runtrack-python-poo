from job04 import Forme
import math

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius

    def aire(self):
        return math.pi * self.radius ** 2

rectangle_instance = Rectangle(largeur=5, hauteur=100)
print("Aire du rectangle:", rectangle_instance.aire())

cercle_instance = Cercle(radius=3)
print("Aire du cercle:", cercle_instance.aire())
