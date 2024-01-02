class Produit:

    def __init__(self, nom, prixHT, TVA=20):
    # Initialise la classe avec (nom, prixHT, TVA=20) où nom est le nom du produit, prixHT est le prix hors taxes et TVA est le taux de TVA par défaut à 20%.
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def calculerPrixTTC(self):
    # Cette méthode calcule le prix TTC en utilisant le taux de TVA.
        prixTTC = self.prixHT * (1 + self.TVA / 100)
        return prixTTC

    def afficher(self):
    # La méthode afficher retourne une représentation sous forme de chaîne de caractères de l'objet.
        return str(self)

    def modifierNom(self, nouveauNom):
    # Les méthodes modifierNom et modifierPrixHT permettent de mettre à jour les attributs nom et prixHT.
        self.nom = nouveauNom

    def modifierPrixHT(self, nouveauPrixHT):
        self.prixHT = nouveauPrixHT

    def getNom(self):
    # Les méthodes getNom, getPrixHT et getTVA permettent d'obtenir les valeurs des attributs.
        return self.nom

    def getPrixHT(self):
        return self.prixHT

    def getTVA(self):
        return self.TVA

    def __str__(self):
    # La méthode spéciale __str__ retourne une représentation sous forme de chaîne de caractères de l'objet.
        return f"Nom: {self.nom}, Prix HT: {self.prixHT}, TVA: {self.TVA}%, Prix TTC: {self.calculerPrixTTC()}"

# Création d'instances de la classe Produit.
produit1 = Produit("Fallout : New Vegas", 9.99)
produit2 = Produit("Cyberpunk 2077", 24.99)
produit3 = Produit("RTX 4080", 1149.0)

print("Informations initiales des produits:")
# Affichage des informations initiales des produits.
print(produit1.afficher())
print(produit2.afficher())
print(produit3.afficher())

# Modification des attributs des produits.
produit1.modifierNom("Fallout 4")
produit1.modifierPrixHT(1.0)

produit2.modifierNom("Payday 2")
produit2.modifierPrixHT(4.99)

produit3.modifierNom("Sims 4")
produit3.modifierPrixHT(59.99)

print("Informations après modification:")
# Affichage des informations après modification.
print(produit1.afficher())
print(produit2.afficher())
print(produit3.afficher())