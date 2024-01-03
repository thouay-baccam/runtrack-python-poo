class Livre:
    # Constructeur de la classe Livre
    def __init__(self, titre, auteur, pages):
        # Initialisation des attributs privés __titre, __auteur et __pages
        self.__titre = titre
        self.__auteur = auteur
        
        # Vérification que le nombre de pages est un entier positif
        if isinstance(pages, int) and pages > 0:
            self.__pages = pages
        else:
            # Affichage d'une erreur si le nombre de pages n'est pas valide
            print("Erreur : Le nombre de pages doit être plus que 0.")
            self.__pages = None

    # Méthode pour obtenir le titre
    def get_titre(self):
        return self.__titre

    # Méthode pour obtenir l'auteur
    def get_auteur(self):
        return self.__auteur

    # Méthode pour obtenir le nombre de pages
    def get_pages(self):
        return self.__pages

    # Méthode pour définir un nouveau titre
    def set_titre(self, nouveau_titre):
        self.__titre = nouveau_titre

    # Méthode pour définir un nouvel auteur
    def set_auteur(self, nouveau_auteur):
        self.__auteur = nouveau_auteur

    # Méthode pour définir un nouveau nombre de pages
    def set_pages(self, nouvelle_pages):
        # Vérification que le nombre de pages est un entier positif
        if isinstance(nouvelle_pages, int) and nouvelle_pages > 0:
            self.__pages = nouvelle_pages
        else:
            # Affichage d'une erreur si le nombre de pages n'est pas valide
            print("Erreur : Le nombre de pages doit être plus que 0.")

# Méthode principale pour éviter la répétition du code dans le job 03
def main():
    # Création d'une instance de la classe Livre avec des valeurs initiales
    mon_livre = Livre("Watchmen", "Alan Moore", 416)

    # Affichage du titre, de l'auteur et du nombre de pages initiaux
    print(f"Titre : {mon_livre.get_titre()}")
    print(f"Auteur : {mon_livre.get_auteur()}")
    print(f"Pages : {mon_livre.get_pages()}")

    # Modification du titre, de l'auteur et du nombre de pages
    mon_livre.set_titre("Le Portrait de Dorian Gray")
    mon_livre.set_auteur("Oscar Wilde")
    mon_livre.set_pages(258)

    # Affichage du titre, de l'auteur et du nombre de pages après modification
    print(f"Titre après modif : {mon_livre.get_titre()}")
    print(f"Auteur après modif : {mon_livre.get_auteur()}")
    print(f"Pages après modif : {mon_livre.get_pages()}")

# Exécution de la méthode principale si le script est exécuté en tant que programme principal
if __name__ == "__main__":
    main()
