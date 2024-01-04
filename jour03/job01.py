class Ville:
    def __init__(self, nom_ville, nombre_habitants):
        self.__nom_ville = nom_ville
        self.__nombre_habitants = nombre_habitants

    def get_nom_ville(self):
        return self.__nom_ville

    def get_nombre_habitants(self):
        return self.__nombre_habitants

    def ajouterPopulation(self):
        self.__nombre_habitants += 1

class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        self.ajouterPopulation()

    def ajouterPopulation(self):
        self.__ville.ajouterPopulation()

paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)

print(f"Population de la ville de {paris.get_nom_ville()} : {paris.get_nombre_habitants()}")
print(f"Population de la ville de {marseille.get_nom_ville()} : {marseille.get_nombre_habitants()}")

john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

print(f"Mise a jour de la population de la ville de {paris.get_nom_ville()} : {paris.get_nombre_habitants()}")
print(f"Mise a jour de la population de la ville de {marseille.get_nom_ville()} : {marseille.get_nombre_habitants()}")