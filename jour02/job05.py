class Voiture:
    def __init__(self, marque, modele, annee, kilometrage, reservoir=50):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = reservoir

    def get_marque(self):
        return self.__marque

    def set_marque(self, nouvelle_marque):
        self.__marque = nouvelle_marque

    def get_modele(self):
        return self.__modele

    def set_modele(self, nouveau_modele):
        self.__modele = nouveau_modele

    def get_annee(self):
        return self.__annee

    def set_annee(self, nouvelle_annee):
        self.__annee = nouvelle_annee

    def get_kilometrage(self):
        return self.__kilometrage

    def set_kilometrage(self, nouveau_kilometrage):
        self.__kilometrage = nouveau_kilometrage

    def get_en_marche(self):
        return "En marche" if self.__en_marche else "Arrêtée"

    def demarrer(self):
        self.__en_marche = self.__verifier_plein()
        if self.__en_marche:
            print("La voiture démarre.")
        else:
            print("La voiture ne démarre pas.")

    def arreter(self):
        self.__en_marche = False
        print("La voiture s'arrête.")

    def get_reservoir(self):
        return self.__reservoir
    
    def set_reservoir(self, nouveau_reservoir):
        self.__reservoir = nouveau_reservoir

    def __verifier_plein(self):
        return self.__reservoir > 5

ma_voiture = Voiture(marque="Audi", modele="TT Coupé", annee=2023, kilometrage=50, reservoir=40)
print(f"Marque: {ma_voiture.get_marque()} / Modèle: {ma_voiture.get_modele()} / Année: {ma_voiture.get_annee()} / Kilométrage: {ma_voiture.get_kilometrage()} / Reservoir : {ma_voiture.get_reservoir()} sur 50")
print(f"La voiture est actuellement: {ma_voiture.get_en_marche()}")
ma_voiture.demarrer()
print(f"La voiture est maintenant: {ma_voiture.get_en_marche()}")
ma_voiture.arreter()
print(f"La voiture est maintenant: {ma_voiture.get_en_marche()}")

ma_voiture.set_marque("Citroen")
ma_voiture.set_modele("C5 X")
ma_voiture.set_annee("2021")
ma_voiture.set_kilometrage("9313")
ma_voiture.set_reservoir(1)

print(f"Marque: {ma_voiture.get_marque()} / Modèle: {ma_voiture.get_modele()} / Année: {ma_voiture.get_annee()} / Kilométrage: {ma_voiture.get_kilometrage()} / Reservoir : {ma_voiture.get_reservoir()} sur 50")
print(f"La voiture est actuellement: {ma_voiture.get_en_marche()}")
ma_voiture.demarrer()
