objet1 = {
    "nom": "jeu",
    "prix": 30,
    "quantite_en_stock": 300,
}

objet2 = {
    "nom": "legume",
    "prix": 3,
    "quantite_en_stock": 100,
}

objet3 = {
    "nom": "tv",
    "prix": 400,
    "quantite_en_stock": 50,
}

objet4 = {
    "nom": "voiture",
    "prix": 2500,
    "quantite_en_stock": 4,
}

liste = [objet1, objet2, objet3, objet4]
for objet in liste:
    prix = objet["prix"]
    quantite = objet["quantite_en_stock"]
    total = prix * quantite
    nom = objet["nom"]
    if (quantite < 5):    
        print(f"Le prix total de {nom} est de {total}€")
