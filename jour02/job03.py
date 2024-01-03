from job02 import Livre

class Biblio(Livre):
    def __init__(self, titre, auteur, pages):
        super().__init__(titre, auteur, pages)
        self.__disponible = True

    def verification(self):
        return self.__disponible

    def emprunter(self):
        if self.verification():
            self.__disponible = False
            print(f"Le livre '{self.get_titre()}' a été emprunté.")
        else:
            print(f"Le livre '{self.get_titre()}' n'est pas disponible pour l'emprunt.")

    def rendre(self):
        if not self.verification():
            self.__disponible = True
            print(f"Le livre '{self.get_titre()}' a été rendu.")
        else:
            print(f"Le livre '{self.get_titre()}' n'a pas été emprunté, donc ne peut pas être rendu.")

if __name__ == "__main__":
    emprunt_livre = Biblio("Le Portrait de Dorian Gray", "Oscar Wilde", 258)
    
    print("Le livre est disponible:", emprunt_livre.verification())
    emprunt_livre.rendre()
    emprunt_livre.emprunter()
    print("Le livre est disponible:", emprunt_livre.verification())
