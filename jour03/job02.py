class CompteBancaire:

    def __init__(self, numero_compte, nom_client, prenom_client, solde_client, decouvert=False):
        self.__numero_compte = numero_compte
        self.__nom_client = nom_client
        self.__prenom_client = prenom_client
        self.__solde_client = solde_client
        self.__decouvert = decouvert

    def afficher(self):
        print(f"\nCompte n°{self.__numero_compte} - {self.__nom_client} {self.__prenom_client}")
        self.afficherSolde()

    def afficherSolde(self):
        print(f"Solde actuel : {self.__solde_client} €")

    def versement(self, montant):
        self.__solde_client += montant
        print(f"Versement de {montant} € effectué !")
        self.afficherSolde()

    def retrait(self, montant):
        if not self.__decouvert and self.__solde_client - montant < 0:
            print("Opération impossible : Solde insuffisant.")
        else:
            self.__solde_client -= montant
            print(f"Retrait de {montant} € effectué !")
            self.afficherSolde()

    def agios(self, taux_agios): 
        if self.__solde_client < 0:
            agios_amount = abs(self.__solde_client) * taux_agios
            self.__solde_client -= agios_amount
            print(f"Agios de {agios_amount} € appliqués.")
            self.afficherSolde()

    def virement(self, compte_dest, montant):
        if self.__solde_client - montant < 0 and not self.__decouvert:
            print("Opération impossible : Solde insuffisant.")
        else:
            self.__solde_client -= montant
            compte_dest.versement(montant)
            print(f"Virement de {montant} € effectué de {self.__prenom_client} {self.__nom_client} à {compte_dest.__prenom_client} {compte_dest.__nom_client}.")
            self.afficherSolde()

# Création des comptes
compte1 = CompteBancaire(numero_compte=19051997, nom_client="Baccam", prenom_client="Teddy", solde_client=2901)
compte1.afficher()

compte1.versement(532)

compte1.retrait(540)

compte2 = CompteBancaire(numero_compte=14111997, nom_client="Cole", prenom_client="Jade", solde_client=-589, decouvert=True)
compte2.afficher()

compte1.agios(0.1)

compte1.virement(compte2, 591)

print("\nInformations après les opérations :")
compte1.afficher()
compte2.afficher()