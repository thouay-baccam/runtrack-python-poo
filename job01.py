class Operation:
    
    def __init__(self, nombre1=40, nombre2=46):
        # Initialise la classe avec deux paramètres par défaut, nombre1 et nombre2
        self.nombre1 = nombre1
        self.nombre2 = nombre2

# Crée une instance de la classe Operation sans fournir d'arguments, utilisant les valeurs par défaut
operation_instance = Operation()

# Affiche l'instance de la classe (représentation par défaut, généralement l'emplacement mémoire)
print(operation_instance)