from job02 import Livre

class Biblio(Livre):
    # Constructeur de la classe Biblio qui hérite de la classe Livre
    def __init__(self, titre, auteur, pages):
        # Appel du constructeur de la classe mère (Livre)
        super().__init__(titre, auteur, pages)
        # Initialisation de l'attribut privé __disponible à True
        self.__disponible = True

    # Méthode pour vérifier la disponibilité du livre
    def verification(self):
        return self.__disponible

    # Méthode pour emprunter le livre
    def emprunter(self):
        # Vérification de la disponibilité du livre
        if self.verification():
            # Si le livre est disponible, le marquer comme emprunté et afficher un message
            self.__disponible = False
            print(f"Le livre '{self.get_titre()}' a été emprunté.")
        else:
            # Si le livre n'est pas disponible, afficher un message
            print(f"Le livre '{self.get_titre()}' n'est pas disponible pour l'emprunt.")

    # Méthode pour rendre le livre
    def rendre(self):
        # Vérification que le livre n'est pas déjà disponible
        if not self.verification():
            # Si le livre n'est pas disponible, le marquer comme rendu et afficher un message
            self.__disponible = True
            print(f"Le livre '{self.get_titre()}' a été rendu.")
        else:
            # Si le livre est déjà disponible, afficher un message
            print(f"Le livre '{self.get_titre()}' n'a pas été emprunté, donc ne peut pas être rendu.")

# Exécution du code si le script est exécuté en tant que programme principal
if __name__ == "__main__":
    # Création d'une instance de la classe Biblio avec des valeurs initiales
    emprunt_livre = Biblio("Le Portrait de Dorian Gray", "Oscar Wilde", 258)
    
    # Affichage de la disponibilité initiale du livre
    print("Le livre est disponible:", emprunt_livre.verification())
    
    # Tentative de rendre le livre (ne devrait pas changer la disponibilité car non emprunté)
    emprunt_livre.rendre()
    
    # Tentative d'emprunter le livre
    emprunt_livre.emprunter()
    
    # Affichage de la disponibilité après l'emprunt (devrait être False)
    print("Le livre est disponible:", emprunt_livre.verification())
    
    # Tentative d'emprunter le livre à nouveau (devrait afficher un message indiquant que le livre n'est pas disponible)
    emprunt_livre.emprunter()
    
    # Tentative de rendre le livre (devrait afficher un message indiquant que le livre n'a pas été emprunté)
    emprunt_livre.rendre()
