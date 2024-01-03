class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}
        self.__statut_commande = "en cours"

    def ajouter_plat(self, nom_plat, prix_plat):
        if nom_plat not in self.__plats_commandes:
            self.__plats_commandes[nom_plat] = {'prix': prix_plat, 'statut': self.__statut_commande}
            print(f"Le plat suivant a été ajouté a la commande : '{nom_plat}'.")

    def annuler_commande(self):
        self.__statut_commande = "annulée"
        print("La commande a été annulée.")

    def calculer_total(self):
        total = sum(plat['prix'] for plat in self.__plats_commandes.values())
        return total

    def afficher_commande(self):
        print(f"Numéro de la commande : {self.__numero_commande}")
        print("Plats commandés:")
        for plat, details in self.__plats_commandes.items():
            print(f"{plat} - Prix: {details['prix']} - Statut: {details['statut']}")
        print(f"Total à payer : {self.calculer_total()}")

    def calculer_tva(self, taux_tva=0.2):
        tva = self.calculer_total() * taux_tva
        return tva

commande1 = Commande(numero_commande=1)
commande1.ajouter_plat("Pizza", 12.50)
commande1.ajouter_plat("Salade", 8.00)
commande1.afficher_commande()
print(f"TVA à payer : {commande1.calculer_tva()}")
commande1.annuler_commande()
commande1.afficher_commande()