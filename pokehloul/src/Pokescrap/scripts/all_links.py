import requests
from lxml import etree

# URL de votre API Django pour les requêtes POST
url_post = "http://127.0.0.1:8000/add-to-scrap/"

# Fonction pour envoyer les données via POST
def post_data(name, type_element, url):
    payload = {
        "name": name,
        "type_element": type_element,
        "url": f"https://www.pokepedia.fr{url}"  # Complète l'URL relative
    }
    response = requests.post(url_post, json=payload)
    if response.status_code == 201:
        print(f"Envoyé avec succès : {name}")
    else:
        print(f"Erreur {response.status_code} pour {name}: {response.json()}")

# Talents
print("Scraping des Talents...")
result = requests.get('https://www.pokepedia.fr/Liste_des_talents')
dom = etree.HTML(result.text)
tableau = dom.xpath("//div/table/tbody/tr/td[3]/a")

for tab in tableau:
    name = tab.text
    url = tab.attrib['href']
    post_data(name, "T", url)  # Type "T" pour Talent

# Capacités
print("\nScraping des Capacités...")
result = requests.get('https://www.pokepedia.fr/Liste_des_capacités')
dom = etree.HTML(result.text)
tableau = dom.xpath("//div/table/tbody/tr/td[3]/a")

for tab in tableau:
    name = tab.text
    url = tab.attrib['href']
    post_data(name, "A", url)  # Type "A" pour Attaque

# Pokémon
print("\nScraping des Pokémon...")
result = requests.get("https://www.pokepedia.fr/Liste_des_Pokémon_dans_l%27ordre_du_Pokédex_National")
dom = etree.HTML(result.text)
tableau = dom.xpath("//div/table/thead/following-sibling::tbody/tr/td/a")

i = 4
for tab in tableau:
    if i % 4 == 0:  # Condition pour sélectionner uniquement les bonnes lignes
        name = tab.text
        url = tab.attrib['href']
        post_data(name, "P", url)  # Type "P" pour Pokémon
    i += 1
