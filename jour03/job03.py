class Tache:
    def __init__(self, titre, description, statut="à faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, titre):
        self.taches = [t for t in self.taches if t.titre != titre]

    def marquerCommeFinie(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                tache.statut = "finie"
                break

    def afficherListe(self):
        return [f"{tache.titre}: {tache.description} - {tache.statut}" for tache in self.taches]

    def filterListe(self, statut):
        return [tache for tache in self.taches if tache.statut == statut]

tache1 = Tache("Faire le jour 03 Python", "Terminer le job 03 et le reste.")
tache2 = Tache("Aller au coiffeur", "Marre des cheveux longs.")
tache3 = Tache("Acheter du PQ", "Car j'ai pas de bidet.")
tache4 = Tache("Trouver une derniere tâche", "Car je sais pas quoi écrire.")

listeDeTaches = ListeDeTaches()

listeDeTaches.ajouterTache(tache1)
listeDeTaches.ajouterTache(tache2)
listeDeTaches.ajouterTache(tache3)
listeDeTaches.ajouterTache(tache4)

print("Liste initiale:")
print(listeDeTaches.afficherListe())

listeDeTaches.supprimerTache("Acheter du PQ")

print("\nListe après la suppression:")
print(listeDeTaches.afficherListe())

listeDeTaches.marquerCommeFinie("Faire le jour 03 Python")

print("\nListe après le marquage comme finie:")
print(listeDeTaches.afficherListe())

taches_a_faire = listeDeTaches.filterListe("à faire")

print("\nReste des tâches à faire:")
print([tache.titre for tache in taches_a_faire])