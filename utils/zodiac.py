# utils/zodiac.py
sign_elements = {
    "Bélier": "Feu",
    "Taureau": "Terre",
    "Gémeaux": "Air",
    "Cancer": "Eau",
    "Lion": "Feu",
    "Vierge": "Terre",
    "Balance": "Air",
    "Scorpion": "Eau",
    "Sagittaire": "Feu",
    "Capricorne": "Terre",
    "Verseau": "Air",
    "Poissons": "Eau"
}

def get_element(signe):
    return sign_elements.get(signe, "Inconnu")
