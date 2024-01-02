class Personne:

    def __init__(self, nom="", prenom=""):
        # Initialise la classe avec deux paramètres par défaut, nom et prénom
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        # Méthode qui renvoie une chaîne de caractères présentant la personne
        return f"Je suis {self.prenom} {self.nom}"

# Crée une instance de la classe Personne avec nom="Doe" et prenom="John"
personne1 = Personne(nom="Doe", prenom="John")

# Crée une instance de la classe Personne avec nom="Dupond" et prenom="Jean"
personne2 = Personne(nom="Dupond", prenom="Jean")

# Appelle la méthode SePresenter pour afficher la présentation de la première personne
print(personne1.SePresenter())

# Appelle la méthode SePresenter pour afficher la présentation de la deuxième personne
print(personne2.SePresenter())