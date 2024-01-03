class Student:
    def __init__(self, prenom, nom, idstudent, credits=0):
        self.__prenom = prenom
        self.__nom = nom
        self.__idstudent = idstudent
        self.__credits = credits
        self.__level = self.__studentEval()

    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
            print(f"{credits} crédits ajoutés avec succès ! ")
            self.__level = self.__studentEval()
        else:
            print("Veuillez entrer un nombre de crédits valide (supérieur à 0).")

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

    def studentInfo(self):
        print(f"Nom: {self.__nom}")
        print(f"Prénom: {self.__prenom}")
        print(f"ID : {self.__idstudent}")
        print(f"Niveau: {self.__level}")


john_doe = Student(prenom="John", nom="Doe", idstudent=145)

john_doe.add_credits(0)
john_doe.studentInfo()

john_doe.add_credits(60)
john_doe.studentInfo()

john_doe.add_credits(19)
john_doe.studentInfo()

john_doe.add_credits(10)
john_doe.studentInfo()

john_doe.add_credits(10)
john_doe.studentInfo()