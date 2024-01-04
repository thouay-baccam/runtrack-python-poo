class CompteBancaire:

    def __init__(self, numero_compte, nom_client, prenom_client, solde_client):
        self.__numero_compte = numero_compte
        self.__nom_client = nom_client
        self.__prenom_client = prenom_client
        self.__solde_client = solde_client

    def afficher(self):
        print(f"Compte n°{self.__numero_compte} - {self.__nom_client} {self.__prenom_client}.")
        self.afficherSolde()

    def afficherSolde(self):
        print(f"Solde actuel du compte : {self.__solde_client} €.")

    def versement(self, montant):
        self.__solde_client += montant
        print(f"Versement de {montant} € effectué avec succès !")
        self.afficherSolde()

    def retrait(self, montant):
        if self.__solde_client - montant < 0:
            print("Opération impossible : Solde insuffisant.)")
        else:
            self.__solde_client -= montant
            print(f"Retrait de {montant} € effectué !")
            self.afficherSolde()

mon_compte = CompteBancaire(numero_compte=19051997, nom_client="Baccam", prenom_client="Teddy", solde_client=2901)
mon_compte.afficher()

mon_compte.versement(532)

mon_compte.retrait(540)