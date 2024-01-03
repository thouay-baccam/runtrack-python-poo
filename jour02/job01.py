class Rectangle:
    # Constructeur de la classe Rectangle
    def __init__(self, longueur, largeur):
        # Initialisation des attributs privés __longueur et __largeur
        self.__longueur = longueur
        self.__largeur = largeur

    # Méthode pour obtenir la longueur
    def get_longueur(self):
        return self.__longueur

    # Méthode pour obtenir la largeur
    def get_largeur(self):
        return self.__largeur
    
    # Méthode pour définir une nouvelle longueur
    def set_longueur(self, nouvelle_longueur):
        self.__longueur = nouvelle_longueur

    # Méthode pour définir une nouvelle largeur
    def set_largeur(self, nouvelle_largeur):
        self.__largeur = nouvelle_largeur

# Création d'une instance de la classe Rectangle avec une longueur de 10 et une largeur de 5
mon_rectangle = Rectangle(10, 5)

# Affichage de la longueur et de la largeur initiales
print(f"Longueur : {mon_rectangle.get_longueur()}")
print(f"Largeur : {mon_rectangle.get_largeur()}")

# Modification de la longueur et de la largeur
mon_rectangle.set_longueur(15)
mon_rectangle.set_largeur(8)

# Affichage de la longueur et de la largeur après modification
print(f"Longueur après modification : {mon_rectangle.get_longueur()}")
print(f"Largeur après modification : {mon_rectangle.get_largeur()}")
