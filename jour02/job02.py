class Livre:
    def __init__(self, titre, auteur, pages):
        self.__titre = titre
        self.__auteur = auteur
        if isinstance(pages, int) and pages > 0:
            self.__pages = pages
        else:
            print("Erreur : Le nombre de pages doit être plus que 0.")
            self.__pages = None

    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_pages(self):
        return self.__pages

    def set_titre(self, nouveau_titre):
        self.__titre = nouveau_titre

    def set_auteur(self, nouveau_auteur):
        self.__auteur = nouveau_auteur

    def set_pages(self, nouvelle_pages):
        if isinstance(nouvelle_pages, int) and nouvelle_pages > 0:
            self.__pages = nouvelle_pages
        else:
            print("Erreur : Le nombre de pages doit être plus que 0.")

    def main(): # Pour pas que le code se rêpete dans le job 03.
        mon_livre = Livre("Watchmen", "Alan Moore", 416)

        print(f"Titre : {mon_livre.get_titre()}")
        print(f"Auteur : {mon_livre.get_auteur()}")
        print(f"Pages : {mon_livre.get_pages()}")

        mon_livre.set_titre("Le Portrait de Dorian Gray")
        mon_livre.set_auteur("Oscar Wilde")
        mon_livre.set_pages(258)

        print(f"Titre après modif : {mon_livre.get_titre()}")
        print(f"Auteur après modif : {mon_livre.get_auteur()}")
        print(f"Pages après modif : {mon_livre.get_pages()}")

    if __name__ == "__main__":
        main()