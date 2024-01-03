class Voiture:
    # Constructeur de la classe Voiture
    def __init__(self, marque, modele, annee, kilometrage, reservoir=50):
        # Initialisation des attributs privés __marque, __modele, __annee, __kilometrage, __en_marche et __reservoir
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = reservoir

    # Méthode pour obtenir la marque
    def get_marque(self):
        return self.__marque

    # Méthode pour définir une nouvelle marque
    def set_marque(self, nouvelle_marque):
        self.__marque = nouvelle_marque

    # Méthode pour obtenir le modèle
    def get_modele(self):
        return self.__modele

    # Méthode pour définir un nouveau modèle
    def set_modele(self, nouveau_modele):
        self.__modele = nouveau_modele

    # Méthode pour obtenir l'année
    def get_annee(self):
        return self.__annee

    # Méthode pour définir une nouvelle année
    def set_annee(self, nouvelle_annee):
        self.__annee = nouvelle_annee

    # Méthode pour obtenir le kilométrage
    def get_kilometrage(self):
        return self.__kilometrage

    # Méthode pour définir un nouveau kilométrage
    def set_kilometrage(self, nouveau_kilometrage):
        self.__kilometrage = nouveau_kilometrage

    # Méthode pour obtenir l'état de la voiture (en marche ou arrêtée)
    def get_en_marche(self):
        return "En marche" if self.__en_marche else "Arrêtée"

    # Méthode pour démarrer la voiture
    def demarrer(self):
        # Vérification que le réservoir est suffisamment plein pour démarrer
        self.__en_marche = self.__verifier_plein()
        if self.__en_marche:
            print("La voiture démarre.")
        else:
            print("La voiture ne démarre pas.")

    # Méthode pour arrêter la voiture
    def arreter(self):
        self.__en_marche = False
        print("La voiture s'arrête.")

    # Méthode pour obtenir le niveau du réservoir
    def get_reservoir(self):
        return self.__reservoir
    
    # Méthode pour définir un nouveau niveau de réservoir
    def set_reservoir(self, nouveau_reservoir):
        self.__reservoir = nouveau_reservoir

    # Méthode privée pour vérifier si le réservoir est suffisamment plein pour démarrer
    def __verifier_plein(self):
        return self.__reservoir > 5

# Création d'une instance de la classe Voiture avec des valeurs initiales
ma_voiture = Voiture(marque="Audi", modele="TT Coupé", annee=2023, kilometrage=50, reservoir=40)

# Affichage des informations initiales de la voiture
print(f"Marque: {ma_voiture.get_marque()} / Modèle: {ma_voiture.get_modele()} / Année: {ma_voiture.get_annee()} / Kilométrage: {ma_voiture.get_kilometrage()} / Reservoir : {ma_voiture.get_reservoir()} sur 50")
print(f"La voiture est actuellement: {ma_voiture.get_en_marche()}")

# Démarrage de la voiture et affichage de son état après démarrage
ma_voiture.demarrer()
print(f"La voiture est maintenant: {ma_voiture.get_en_marche()}")

# Arrêt de la voiture et affichage de son état après arrêt
ma_voiture.arreter()
print(f"La voiture est maintenant: {ma_voiture.get_en_marche()}")

# Modification des attributs de la voiture
ma_voiture.set_marque("Citroen")
ma_voiture.set_modele("C5 X")
ma_voiture.set_annee(2021)
ma_voiture.set_kilometrage(9313)
ma_voiture.set_reservoir(1)

# Affichage des informations de la voiture après modification
print(f"Marque: {ma_voiture.get_marque()} / Modèle: {ma_voiture.get_modele()} / Année: {ma_voiture.get_annee()} / Kilométrage: {ma_voiture.get_kilometrage()} / Reservoir : {ma_voiture.get_reservoir()} sur 50")
print(f"La voiture est actuellement: {ma_voiture.get_en_marche()}")

# Démarrage de la voiture après modification et affichage de son état
ma_voiture.demarrer()
