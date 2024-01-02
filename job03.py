class Operation:
    
    def __init__(self, nombre1=40, nombre2=46):
        # Initialise la classe avec deux paramètres par défaut, nombre1 et nombre2
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        # Méthode qui effectue l'addition des deux nombres et affiche le résultat
        result = self.nombre1 + self.nombre2
        print("Le résultat est :", result)

# Crée une instance de la classe Operation sans fournir d'arguments, utilisant les valeurs par défaut
operation_instance = Operation()

# Appelle la méthode addition de l'instance, effectuant l'addition et affichant le résultat
operation_instance.addition()