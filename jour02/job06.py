class Commande:
    def __init__(self, numero_commande, liste_commande, taux_tva=0.20):
        # Initialisation des attributs de la commande
        self.__numero_commande = numero_commande
        self.__liste_commande = liste_commande
        self.__statut_commande = "En cours"
        self.__prix_ht = self.__calculer_prix_ht()
        self.__TAUX_TVA = taux_tva
        self.__tva = self.__calculer_tva()

    def __calculer_tva(self):
        # Méthode privée pour calculer la TVA
        return self.__prix_ht * self.__TAUX_TVA

    def __calculer_prix_ht(self):
        # Méthode privée pour calculer le prix hors taxe
        return sum(self.__liste_commande.values())

    def ajouter_a_commande(self, plat, prix):
        # Méthode pour ajouter un plat à la commande
        self.__liste_commande[plat] = prix
        self.__prix_ht = self.__calculer_prix_ht()
        self.__tva = self.__calculer_tva()

    def finaliser_commande(self):
        # Méthode pour finaliser une commande
        self.__statut_commande = "Terminée"

    def annuler_commande(self):
        # Méthode pour annuler une commande
        self.__statut_commande = "Annulée"

    def infos_commande(self):
        # Méthode pour afficher les informations de la commande
        infos_commande = (
            f"Numéro de commande : {self.__numero_commande}\n"
            f"Statut de la commande : {self.__statut_commande}\n"
            f"----------------\n"
        )
        for plat, prix in self.__liste_commande.items():
            infos_commande += f"- {plat}: {prix}€\n"
        infos_commande += (
            f"----------------\n"
            f"Prix hors-taxe : {self.__prix_ht}€\n"
            f"TVA : {self.__tva}€\n"
            f"Total : {self.__prix_ht + self.__tva}€\n"
        )
        return infos_commande


def tester_commande():
    # Fonction de test
    premiere_commande = {
        "Filet de saumon grillé": 22.50,
        "Risotto aux truffes": 18.80,
        "Tarte au citron meringuée": 8.50,
    }
    premiere = Commande(1, premiere_commande)
    print(premiere.infos_commande())

    premiere.ajouter_a_commande("Champagne brut", 45.00)
    print(premiere.infos_commande())

    premiere.annuler_commande()
    print(premiere.infos_commande())

    deuxieme_commande = {
        "Côte de bœuf Wagyu": 120.00,
        "Homard grillé au beurre": 58.90,
        "Soufflé au chocolat noir": 12.50,
    }
    deuxieme = Commande(2, deuxieme_commande, taux_tva=0.25)
    print(deuxieme.infos_commande())

    deuxieme.ajouter_a_commande("Bouteille de vin rouge Grand Cru", 75.00)
    print(deuxieme.infos_commande())

    deuxieme.finaliser_commande()
    print(deuxieme.infos_commande())


if __name__ == "__main__":
    tester_commande()