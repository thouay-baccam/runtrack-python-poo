class Vehicule:

    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print(f"Marque = {self.marque}")
        print(f"Modèle = {self.modele}")
        print(f"Année = {self.annee}")
        print(f"Prix = {self.prix}")

    def demarrer(self):
        print("Attention, je roule")

class Voiture(Vehicule):

    def __init__(self, marque, modele, annee, prix, portes=4):
        super().__init__(marque, modele, annee, prix)
        self.portes = portes

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes = {self.portes}")
    
    def demarrer(self):
        print(f"La {self.marque} {self.modele} démarre et elle fonce!\n")

class Moto(Vehicule):

    def __init__(self, marque, modele, annee, prix, portes=2):
        super().__init__(marque, modele, annee, prix)
        self.portes = portes

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes = {self.portes}")

    def demarrer(self):
        print(f"La {self.marque} {self.modele} démarre et atteint 100km/h rapidement !")


mercedes = Voiture(marque="Mercedes", modele="Classe A", annee=2020, prix=18500)
mercedes.informationsVehicule()
mercedes.demarrer()

yamaha = Moto(marque="Yamaha", modele="1200 Vmax", annee=1987, prix=4500)
yamaha.informationsVehicule()
yamaha.demarrer()
