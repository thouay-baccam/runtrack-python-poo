class Point:
    
    def __init__(self, x, y):
        # Initialise la classe avec deux coordonnées, x et y
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        # Méthode qui affiche les coordonnées du point
        print(f"Coordonnées: ({self.x}, {self.y})")

    def afficherX(self):
        # Méthode qui affiche la coordonnée x du point
        print(f"X-Coordonnée: {self.x}")

    def afficherY(self):
        # Méthode qui affiche la coordonnée y du point
        print(f"Y-Coordonnée: {self.y}")

    def changerX(self, new_x):
        # Méthode qui modifie la coordonnée x du point avec une nouvelle valeur
        self.x = new_x

    def changerY(self, new_y):
        # Méthode qui modifie la coordonnée y du point avec une nouvelle valeur
        self.y = new_y

# Crée une instance de la classe Point avec les coordonnées (3, 5)
cord = Point(3, 5)

# Affiche les coordonnées du point initial
cord.afficherLesPoints()

# Affiche la coordonnée x du point initial
cord.afficherX()

# Affiche la coordonnée y du point initial
cord.afficherY()

# Modifie la coordonnée x du point avec une nouvelle valeur (7)
cord.changerX(7)

# Modifie la coordonnée y du point avec une nouvelle valeur (10)
cord.changerY(10)

# Affiche les nouvelles coordonnées du point après les modifications
cord.afficherLesPoints()