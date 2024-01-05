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
    def __init__(self, nom_equipe):
        self.nom_equipe = nom_equipe
        self.liste_joueurs = []

    def ajouterJoueur(self, joueur):
        self.liste_joueurs.append(joueur)
        print(f"{joueur.nom_joueur} a été ajouté à l'équipe {self.nom_equipe}.")

    def afficherStatistiquesJoueurs(self):
        print(f"\nStatistiques des joueurs de l'équipe {self.nom_equipe}:")
        for joueur in self.liste_joueurs:
            print(f"{joueur.nom_joueur}: Buts - {joueur.buts_marques}, Passes décisives - {joueur.passes_decisives}, Cartons jaunes - {joueur.cartons_jaunes}, Cartons rouges - {joueur.cartons_rouges}")

    def mettreAJourStatistiquesJoueur(self, nom_joueur, buts=0, passes=0, cartons_jaunes=0, cartons_rouges=0):
        for joueur in self.liste_joueurs:
            if joueur.nom_joueur == nom_joueur:
                joueur.buts_marques += buts
                joueur.passes_decisives += passes
                joueur.cartons_jaunes += cartons_jaunes
                joueur.cartons_rouges += cartons_rouges
                print(f"Statistiques de {joueur.nom_joueur} mises à jour.")

    def determinerGagnant(equipe1, equipe2):
        total_buts_equipe1 = sum(joueur.buts_marques for joueur in equipe1.liste_joueurs)
        total_buts_equipe2 = sum(joueur.buts_marques for joueur in equipe2.liste_joueurs)

        if total_buts_equipe1 > total_buts_equipe2:
            return f"{equipe1.nom_equipe} remporte le match avec un score de {total_buts_equipe1}-{total_buts_equipe2}!"
        elif total_buts_equipe1 < total_buts_equipe2:
            return f"{equipe2.nom_equipe} remporte le match avec un score de {total_buts_equipe2}-{total_buts_equipe1}!"
        else:
            return "Match nul! Aucune équipe n'a remporté le match."

    def nouveauMatch(self):
        for joueur in self.liste_joueurs:
            joueur.buts_marques = 0
            joueur.passes_decisives = 0
            joueur.cartons_jaunes = 0
            joueur.cartons_rouges = 0
        print(f"\nNouveau match pour l'équipe {self.nom_equipe}.")

# Création de Manchester + joueurs

equipe_manchester = Equipe("Manchester United")

attaquant_manchester = Joueur("Marcus Rashford", 10, "Attaquant")
milieu_manchester = Joueur("Paul Pogba", 6, "Milieu de terrain")
defenseur_manchester = Joueur("Luke Shaw", 23, "Défenseur")
gardien_manchester = Joueur("Dean Henderson", 26, "Gardien de but")

equipe_manchester.ajouterJoueur(attaquant_manchester)
equipe_manchester.ajouterJoueur(milieu_manchester)
equipe_manchester.ajouterJoueur(defenseur_manchester)
equipe_manchester.ajouterJoueur(gardien_manchester)

equipe_manchester.afficherStatistiquesJoueurs()

# Création de Liverpool + joueurs

equipe_liverpool = Equipe("Liverpool FC")

attaquant_liverpool = Joueur("Mohamed Salah", 11, "Attaquant")
milieu_liverpool = Joueur("Jordan Henderson", 14, "Milieu de terrain")
defenseur_liverpool = Joueur("Andrew Robertson", 26, "Défenseur")
gardien_liverpool = Joueur("Alisson Becker", 1, "Gardien de but")

equipe_liverpool.ajouterJoueur(attaquant_liverpool)
equipe_liverpool.ajouterJoueur(milieu_liverpool)
equipe_liverpool.ajouterJoueur(defenseur_liverpool)
equipe_liverpool.ajouterJoueur(gardien_liverpool)

equipe_liverpool.afficherStatistiquesJoueurs()

# Match n°1
print("\nManchester United vs Liverpool FC (Match n°1):")

milieu_manchester.effectuerUnePasseDecisive()
attaquant_manchester.marquerUnBut()
gardien_manchester.recevoirUnCartonJaune()
attaquant_liverpool.marquerUnBut()
defenseur_liverpool.recevoirUnCartonRouge()
milieu_liverpool.marquerUnBut()

message_resultat = equipe_manchester.determinerGagnant(equipe_liverpool)
print("\nRésultat du match:", message_resultat)

# Initialisation d'un nouveau match
equipe_manchester.nouveauMatch()
equipe_liverpool.nouveauMatch()

# Match n°2
print("\nManchester United vs Liverpool FC (Match n°2):")

milieu_manchester.effectuerUnePasseDecisive()
attaquant_manchester.marquerUnBut()
defenseur_manchester.marquerUnBut()
attaquant_liverpool.marquerUnBut()
milieu_liverpool.marquerUnBut()

message_resultat = equipe_manchester.determinerGagnant(equipe_liverpool)
print("\nRésultat du match:", message_resultat)