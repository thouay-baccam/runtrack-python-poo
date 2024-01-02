class Personnage:

    def __init__(self, x, y):
        # Initialise la classe avec les coordonnées x et y du personnage
        self.x = x
        self.y = y

    def gauche(self):
        # Méthode qui déplace le personnage d'une unité vers la gauche
        self.x -= 1

    def droite(self):
        # Méthode qui déplace le personnage d'une unité vers la droite
        self.x += 1

    def haut(self):
        # Méthode qui déplace le personnage d'une unité vers le haut
        self.y -= 1

    def bas(self):
        # Méthode qui déplace le personnage d'une unité vers le bas
        self.y += 1

    def position(self):
        # Méthode qui renvoie les coordonnées actuelles du personnage
        return (self.x, self.y)

# Crée une instance de la classe Personnage avec les coordonnées initiales (0, 0)
personnage = Personnage(0, 0)

personnage.droite() # On va a droite pour modifier la valeur de x
print(personnage.position())

personnage.haut() # On fait pareil pour modifier la valeur de y
print(personnage.position())

personnage.gauche() # Puis on retourne a 0 horizontalement en allant a gauche
print(personnage.position())

personnage.bas() # Et on retourne a 0 verticalement en allant en bas
print(personnage.position())






