class Personne:
    def __init__(self, age=19):
        self.age = age

    def afficherAge(self):
        print(f"Age de la personne: {self.age}\n")

    def bonjour(self):
        print("Bonjour!")

    def modifierAge(self, nouvelleage):
        self.age = nouvelleage


class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en kickoff.\n")

    def afficherAge(self):
        print(f"J'ai {self.age} ans")


class Professeur(Personne):
    def __init__(self, matiereEnseignee, age=26):
        super().__init__(age)
        self.matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print(f"Le kick-off {self.matiereEnseignee} va commencer, connectez-vous au Meet.")

personne1 = Personne()
personne1.afficherAge()
personne1.bonjour()
personne1.modifierAge(25)
personne1.afficherAge()

eleve1 = Eleve()
eleve1.afficherAge()
eleve1.allerEnCours()

professeur1 = Professeur(matiereEnseignee="Cybersecurité", age=26)
professeur1.enseigner()