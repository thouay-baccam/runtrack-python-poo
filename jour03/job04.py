class Joueur:
    def __init__(self, nom_joueur, numero_joueur, poste):
        self.nom_joueur = nom_joueur
        self.numero_joueur = numero_joueur
        self.poste = poste
        self.buts_marques = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquerUnBut(self):
        self.buts_marques += 1
        print(f"{self.nom_joueur} a marqué un but!!")

    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1
        print(f"{self.nom_joueur} a réalisé une passe décisive!")

    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1
        print(f"{self.nom_joueur} a reçu un carton jaune, ça fait du mal à voir!")

    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1
        print(f"{self.nom_joueur} a reçu un carton rouge, quelle honte!")

class Equipe:
    def __init__(self, nom_joueur):
        self.nom_joueur = nom_joueur
        self.liste_joueurs = []

    def afficherEffectif(self):
        print(f"\nEffectif de l'équipe {self.nom_joueur}:")
        for joueur in self.liste_joueurs:
            print(f"- {joueur.nom_joueur} (Numéro {joueur.numero_joueur}, poste {joueur.poste})")

equipe = Equipe("Manchester United")

joueur1 = Joueur("Anthony Martial", 9, "Attaquant")
joueur2 = Joueur("Casemiro", 18, "Milieu de terrain")

joueur1.marquerUnBut()
joueur1.effectuerUnePasseDecisive()
joueur2.recevoirUnCartonJaune()

equipe.afficherEffectif()