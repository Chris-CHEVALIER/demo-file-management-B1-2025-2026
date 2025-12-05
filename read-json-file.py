import json

""" bel_riose = {
    "first_name": "Bel",
    "last_name": "Riose",
    "gender": "homme",
    "age": 48,
    "role": "commandant",
}

# Sauvegarde
with open("member.json", "w") as file:
    json.dump(bel_riose, file, indent=2) 

# Chargement
with open("member.json", "r") as file:
    data = json.load(file)
    print(data)"""

try:
    with open("members.json", "r") as file:
        print(json.load(file))
except FileNotFoundError:
    print("Le fichier à charger n'a pas été trouvé")
