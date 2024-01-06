from job01 import Eleve, Professeur

eleve1 = Eleve()
eleve1.bonjour()
eleve1.allerEnCours()
eleve1.modifierAge(15)
eleve1.afficherAge()

professeur1 = Professeur(matiereEnseignee="Cybersecurité", age=26)
professeur1.bonjour()
professeur1.enseigner()
professeur1.afficherAge()