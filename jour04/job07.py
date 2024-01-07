import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def afficher_carte(self, montrer_valeur=True):
        # Affiche la carte avec la valeur spéciale pour les figures si demandé.
        if montrer_valeur:
            print(f"{self.valeur} de {self.couleur}")

    def valeur_carte(self):
        # Renvoie la valeur de la carte en tenant compte des règles du blackjack.
        if self.valeur.isdigit():
            return int(self.valeur)
        elif self.valeur in ['Valet', 'Dame', 'Roi']:
            return 10
        elif self.valeur == 'As':
            return 11  # La valeur de l'As est initialement 11, mais peut devenir 1 si nécessaire.

class Jeu:
    def __init__(self):
        # Commence une partie avec un deck de 52 cartes et mélange du paquet.
        self.paquet = [Carte(v, c) for c in ['Cœur', 'Carreau', 'Trèfle', 'Pique'] for v in
                       ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']]
        self.melanger()

    def melanger(self):
        # Mélange le paquet de cartes.
        random.shuffle(self.paquet)

    def tirer_carte(self):
        # Tire une carte du paquet, retourne None si le paquet est vide. (ce qui devrait être impossible)
        return self.paquet.pop() if self.paquet else None

class Partie:
    def __init__(self):
        self.recommencer = True

    def jouer(self):
        while self.recommencer:
            self.recommencer = False
            jeu = Jeu()
            joueur_main, croupier_main = [jeu.tirer_carte() for _ in range(2)], [jeu.tirer_carte(), jeu.tirer_carte()]

            print("Main du joueur :")
            self.afficher_main(joueur_main)

            # Montre la première carte du croupier.
            print("\nMain du croupier :")
            self.afficher_main([croupier_main[0]], montrer_toutes=False)
            print("Carte cachée")

            # Vérifie si le joueur ou le croupier a 21 dès le début.
            if self.calculer_points(joueur_main) == 21:
                print("Félicitations ! Vous avez 21. Vous gagnez.")
                self.recommencer_partie()
                continue
            elif self.calculer_points(croupier_main) == 21:
                print("Le croupier a 21. Vous avez perdu.")
                self.recommencer_partie()
                continue

            while self.demander_coup():
                joueur_main.append(jeu.tirer_carte())
                print("Nouvelle carte :")
                self.afficher_main([joueur_main[-1]])

                joueur_points = self.calculer_points(joueur_main)
                if joueur_points == 21:
                    print("Félicitations ! Vous avez 21. Vous gagnez.")
                    self.recommencer_partie()
                    break
                elif joueur_points > 21:
                    print("Vous avez dépassé 21. Vous avez perdu.")
                    self.recommencer_partie()
                    break

            print("\nMain du croupier :")
            self.afficher_main(croupier_main, montrer_toutes=True)

            while self.calculer_points(croupier_main) < 17:
                croupier_main.append(jeu.tirer_carte())
                print("Nouvelle carte du croupier :")
                self.afficher_main([croupier_main[-1]], montrer_toutes=False)

            self.declarer_resultat(joueur_main, croupier_main)

            self.recommencer_partie()

    def demander_coup(self):
        # Demande au joueur s'il veut prendre une carte supplémentaire.
        return input("Voulez-vous prendre une carte ? (o/n) ").lower() == 'o'

    def calculer_points(self, main):
        # Calcule le total des points d'une main, gère les As comme 1 ou 11.
        points, as_count = 0, 0

        for carte in main:
            points += carte.valeur_carte()

            # Si la carte est un As et le total dépasse 21, réduisez la valeur de l'As à 1.
            if carte.valeur == 'As' and points > 21:
                points -= 10

        return points

    def afficher_main(self, main, montrer_toutes=True):
        # Affiche la main avec le total des points si demandé.
        if montrer_toutes:
            total_points = self.calculer_points(main)
            print(f"Total des points : {total_points}")
            for carte in main:
                carte.afficher_carte()
        else:
            print(f"{main[0].valeur} de {main[0].couleur}\nCarte cachée")

    def declarer_resultat(self, joueur_main, croupier_main):
        # Montre le résultat de la partie.
        print("\nRésultat :")
        print("Main du joueur :")
        self.afficher_main(joueur_main)
        joueur_points = self.calculer_points(joueur_main)
        print(f"Total des points du joueur : {joueur_points}")

        print("\nMain du croupier :")
        self.afficher_main(croupier_main)

        croupier_points = self.calculer_points(croupier_main)
        print(f"Total des points du croupier : {croupier_points}")

        resultat = "Le croupier gagne." if joueur_points > 21 or (croupier_points <= 21 and croupier_points > joueur_points) else \
                   "Le joueur gagne." if croupier_points > 21 or joueur_points > croupier_points else "Égalité."

        print(resultat)

    def recommencer_partie(self):
        # Demande au joueur d'appuyer sur Entrée pour recommencer.
        input("Appuyez sur Entrée pour recommencer...")
        self.recommencer = True

# Exécution du jeu.
partie = Partie()
partie.jouer()