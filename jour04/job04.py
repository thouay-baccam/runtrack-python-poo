class Forme:

    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

rectangle_instance = Rectangle(largeur=5, hauteur=100)
print(rectangle_instance.aire())