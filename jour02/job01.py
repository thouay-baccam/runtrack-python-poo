class Rectangle:
    
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur
    
    def set_longueur(self, nouvelle_longueur):
        self.__longueur = nouvelle_longueur

    def set_largeur(self, nouvelle_largeur):
        self.__largeur = nouvelle_largeur

mon_rectangle = Rectangle(10, 5)

print(f"Longueur : {mon_rectangle.get_longueur()}")
print(f"Largeur : {mon_rectangle.get_largeur()}")

mon_rectangle.set_longueur(15)
mon_rectangle.set_largeur(8)

print(f"Longueur après modif : {mon_rectangle.get_longueur()}")
print(f"Largeur après modif : {mon_rectangle.get_largeur()}")