class Student:
    # Constructeur de la classe Student
    def __init__(self, prenom, nom, idstudent, credits=0):
        # Initialisation des attributs privés __prenom, __nom, __idstudent, __credits et __level
        self.__prenom = prenom
        self.__nom = nom
        self.__idstudent = idstudent
        self.__credits = credits
        # Appel de la méthode privée __studentEval pour déterminer le niveau initial
        self.__level = self.__studentEval()

    # Méthode pour ajouter des crédits au compte de l'étudiant
    def add_credits(self, credits):
        # Vérification que le nombre de crédits ajoutés est positif
        if credits > 0:
            # Ajout des crédits et mise à jour du niveau en appelant la méthode privée __studentEval
            self.__credits += credits
            print(f"{credits} crédits ajoutés avec succès ! ")
            self.__level = self.__studentEval()
        else:
            print("Veuillez entrer un nombre de crédits valide (supérieur à 0).")

    # Méthode privée pour évaluer le niveau de l'étudiant en fonction du nombre de crédits
    def __studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    # Méthode pour afficher les informations de l'étudiant
    def studentInfo(self):
        print(f"Nom: {self.__nom}")
        print(f"Prénom: {self.__prenom}")
        print(f"ID : {self.__idstudent}")
        print(f"Niveau: {self.__level}")

# Création d'une instance de la classe Student avec des valeurs initiales
john_doe = Student(prenom="John", nom="Doe", idstudent=145)

# Ajout de 0 crédit (devrait afficher un message d'erreur) et affichage des informations de l'étudiant
john_doe.add_credits(0)
john_doe.studentInfo()

# Ajout de 60 crédits et affichage des informations de l'étudiant
john_doe.add_credits(60)
john_doe.studentInfo()

# Ajout de 19 crédits et affichage des informations de l'étudiant
john_doe.add_credits(19)
john_doe.studentInfo()

# Ajout de 10 crédits et affichage des informations de l'étudiant
john_doe.add_credits(10)
john_doe.studentInfo()

# Ajout de 10 crédits et affichage des informations de l'étudiant
john_doe.add_credits(10)
john_doe.studentInfo()
