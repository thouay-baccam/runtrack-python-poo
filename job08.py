import math

class Cercle:

    def __init__(self, rayon):
        # Initialise la classe avec le rayon du cercle
        self.rayon = rayon

    def changerRayon(self, nouveau_rayon):
        # Méthode qui modifie le rayon du cercle avec une nouvelle valeur
        self.rayon = nouveau_rayon

    def afficherInfos(self):
        # Méthode qui affiche les informations sur le cercle
        print(f"Cercle de rayon {self.rayon}")

    def circonference(self):
        # Méthode qui calcule la circonférence du cercle
        return 2 * math.pi * self.rayon

    def aire(self):
        # Méthode qui calcule l'aire du cercle
        return math.pi * (self.rayon ** 2)

    def diametre(self):
        # Méthode qui calcule le diamètre du cercle
        return 2 * self.rayon

# Crée une instance de la classe Cercle avec un rayon de 4
cercle1 = Cercle(4)

# Affiche les informations sur le cercle 1
cercle1.afficherInfos()

# Affiche la circonférence, le diamètre et l'aire du cercle 1
print(f"Circonférence du cercle 1 : {cercle1.circonference()}")
print(f"Diamètre du cercle 1 : {cercle1.diametre()}")
print(f"Aire du cercle 1 : {cercle1.aire()}")

# Crée une instance de la classe Cercle avec un rayon de 7
cercle2 = Cercle(7)

# Affiche les informations sur le cercle 2
cercle2.afficherInfos()

# Affiche la circonférence, le diamètre et l'aire du cercle 2
print(f"Circonférence du cercle 2 : {cercle2.circonference()}")
print(f"Diamètre du cercle 2 : {cercle2.diametre()}")
print(f"Aire du cercle 2 : {cercle2.aire()}")