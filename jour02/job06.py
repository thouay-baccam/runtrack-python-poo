class Commande:
    def __init__(self, numero_commande, liste_commande, taux_tva=0.20):
        # Initialise les attributs de la commande
        self._numero_commande = numero_commande
        self._liste_commande = liste_commande
        self._statut_commande = "En cours"
        self._TAUX_TVA = taux_tva
        self._prix_ht = self._calculer_prix_ht()
        self._tva = self._calculer_tva()

    def _calculer_tva(self):
        # Méthode privée pour calculer la TVA
        return self._prix_ht * self._TAUX_TVA

    def _calculer_prix_ht(self):
        # Méthode privée pour calculer le prix hors taxe
        return sum(self._liste_commande.values())

    def _calculer_prix(self):
        # Méthode privée pour mettre à jour le prix total et la TVA
        self._prix_ht = self._calculer_prix_ht()
        self._tva = self._calculer_tva()

    def ajouter_plat(self, plat, prix):
        # Méthode pour ajouter un plat à la commande
        self._liste_commande[plat] = prix
        self._calculer_prix()

    def finaliser_commande(self):
        # Méthode pour finaliser une commande
        self._statut_commande = "Terminée"

    def annuler_commande(self):
        # Méthode pour annuler une commande
        self._statut_commande = "Annulée"

    def afficher_infos(self):
        # Méthode pour afficher les informations de la commande
        infos_commande = (
            f"Numéro de commande : {self._numero_commande}\n"
            f"Statut de la commande : {self._statut_commande}\n"
            f"----------------\n"
        )
        for plat, prix in self._liste_commande.items():
            infos_commande += f"- {plat}: {prix}€\n"
        infos_commande += (
            f"----------------\n"
            f"Prix hors-taxe : {self._prix_ht}€\n"
            f"TVA : {self._tva}€\n"
            f"Total : {self._prix_ht + self._tva}€\n"
        )
        return infos_commande


def tester_commande():
    # Fonction pour tester tout
    premiere_commande = {
        "Filet de saumon grillé": 22.50,
        "Risotto aux truffes": 18.80,
        "Tarte au citron meringuée": 8.50,
    }
    premiere = Commande(1, premiere_commande)
    print(premiere.afficher_infos())

    premiere.ajouter_plat("Champagne brut", 45.00)
    print(premiere.afficher_infos())

    premiere.annuler_commande()
    print(premiere.afficher_infos())

    deuxieme_commande = {
        "Côte de bœuf Wagyu": 120.00,
        "Homard grillé au beurre": 58.90,
        "Soufflé au chocolat noir": 12.50,
    }
    deuxieme = Commande(2, deuxieme_commande, taux_tva=0.25)
    print(deuxieme.afficher_infos())

    deuxieme.ajouter_plat("Bouteille de vin rouge Grand Cru", 75.00)
    print(deuxieme.afficher_infos())

    deuxieme.finaliser_commande()
    print(deuxieme.afficher_infos())


if __name__ == "__main__":
    tester_commande()