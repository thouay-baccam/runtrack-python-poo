from random import choice

class Personnage:
    def __init__(self, nom_personnage, hp_personnage):
        self.nom_personnage = nom_personnage
        self.hp_personnage = hp_personnage

    def perdre_hp(self, degats):
        self.hp_personnage -= degats

    def attaquer(self, cible):
        degats = choice(range(0, 3))
        cible.perdre_hp(degats)
        return degats

class Jeu:
    personnage_disponible = {
        "1": "Scorpion",
        "2": "Sub-Zero",
        "3": "Liu Kang",
        "4": "Raiden",
        "5": "Johnny Cage"
    }

    difficulte_disponible = {
        "1": ("Facile", 12, 8, "Reptile"),
        "2": ("Intermédiaire", 10, 10, "Noob Saibot"),
        "3": ("Difficile", 8, 10, "Shao Kahn"),
        "4": ("Personnalisé", None, None, "Shang Tsung")
    }

    def __init__(self):
        self.personnage = self.choix_personnage()
        self.difficulte = self.choisirNiveau()
        self.lancerJeu()

    def choix_personnage(self):
        print("__________________________")
        while True:
            choix_personnage = input(
                f"Choisissez votre personnage :\n"
                f"1) Scorpion\n"
                f"2) Sub-Zero\n"
                f"3) Liu Kang\n"
                f"4) Raiden\n"
                f"5) Johnny Cage\n"
                f"__________________________\n"
            )
            if choix_personnage in self.personnage_disponible:
                return Personnage(self.personnage_disponible[choix_personnage], 0)
            else:
                print("Choix invalide.\n")

    def choisirNiveau(self):
        print("__________________________")
        while True:
            choisirNiveau = input(
                f"Choisissez la difficulté :\n"
                f"1) Facile\n"
                f"2) Intermédiaire\n"
                f"3) Difficile\n"
                f"4) Personnalisé\n"
                f"__________________________\n"
            )
            if choisirNiveau in self.difficulte_disponible:
                if choisirNiveau == "4":
                    return self.personnaliser_difficulte()
                else:
                    return self.difficulte_disponible[choisirNiveau]
            else:
                print("Choix invalide.\n")

    def personnaliser_difficulte(self):
        try:
            joueur_hp = int(input("Entrez les points de vie du joueur : "))
            ennemi_hp = int(input("Entrez les points de vie de l'ennemi : "))
            if joueur_hp <= 0 or ennemi_hp <= 0:
                print("Les points de vie doivent être supérieurs à zéro.")
                return self.choisirNiveau()
            else:
                return "Personnalisé", joueur_hp, ennemi_hp, "Shang Tsung"
        except ValueError:
            print("Veuillez entrer des nombres valides.")
            return self.choisirNiveau()

    def lancerJeu(self):
        print("__________________________")
        nom_personnage_joueur = self.personnage.nom_personnage
        hp_personnage_joueur, hp_personnage_ennemi, ennemi_nom_personnage = self.difficulte[1], self.difficulte[2], self.difficulte[3]

        joueur = Personnage(nom_personnage_joueur, hp_personnage_joueur)
        ennemi = Personnage(ennemi_nom_personnage, hp_personnage_ennemi)

        print(f"Un Kombat commence entre {joueur.nom_personnage} et {ennemi.nom_personnage}!")

        while True:
            print(
                f"{joueur.nom_personnage}: {joueur.hp_personnage} HP\n"
                f"{ennemi.nom_personnage}: {ennemi.hp_personnage} HP\n"
                "__________________________"
            )

            input("Appuyez sur Entrée pour attaquer...\n")

            degats_joueur = joueur.attaquer(ennemi)
            print(f"L'attaque de {joueur.nom_personnage} inflige {degats_joueur} points de dégâts à {ennemi.nom_personnage}.")

            degats_ennemi = ennemi.attaquer(joueur)
            print(f"{ennemi.nom_personnage} contre-attaque et inflige {degats_ennemi} points de dégâts à {joueur.nom_personnage}.\n")

            if joueur.hp_personnage <= 0 and ennemi.hp_personnage <= 0:
                print("Match nul! Les deux Kombattants sont à terre.")
                break
            elif joueur.hp_personnage <= 0:
                print(f"{joueur.nom_personnage} est mort. {ennemi_nom_personnage} gagne!")
                break
            elif ennemi.hp_personnage <= 0:
                print(f"{ennemi.nom_personnage} est mort. {joueur.nom_personnage} gagne!")
                break

game = Jeu()