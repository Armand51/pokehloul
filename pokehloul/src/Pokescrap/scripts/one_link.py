import requests
from lxml import etree


def scrap_pokemon(url):
    result = requests.get(url)
    dom = etree.HTML(result.text)
    payload = {
        "name": dom.xpath("//h1/span")[0].text,
        "picture_url": "https://www.pokepedia.fr/" + dom.xpath("""//tbody/tr/td[@class="illustration"]/span/a/img""")[0].attrib['src'],
        "url": url
    }
    response = requests.post("http://127.0.0.1:8000/add-to-data/P", json=payload)
    if response.status_code == 201:
        print("Envoyé avec succès ")
    else:
        print(f"Erreur {response.status_code} : {response.json()}")




def scrap_talent(url):
    result = requests.get(url)
    dom = etree.HTML(result.text)
    payload = {
        "name": dom.xpath("//h1/span")[0].text,
        "url": url,
        "description": dom.xpath("//td[@class='précision']")[0].text,
        "effet_combat": dom.xpath("//span[text()='En combat']/ancestor-or-self::th/following-sibling::td")[0].text,
        "effet_terrain": dom.xpath("//span[text()='Terrain']/ancestor-or-self::th/following-sibling::td")[0].text,
    }
    response = requests.post("http://127.0.0.1:8000/add-to-data/T", json=payload)
    if response.status_code == 201:
        print("Envoyé avec succès ")
    else:
        print(f"Erreur {response.status_code} : {response.json()}")




def scrap_attaque(url):
    result = requests.get(url)
    dom = etree.HTML(result.text)
    payload = {
        "name": dom.xpath("//h1/span")[0].text,
        "url": url
    }
    response = requests.post("http://127.0.0.1:8000/add-to-data/A", json=payload)
    if response.status_code == 201:
        print("Envoyé avec succès ")
    else:
        print(f"Erreur {response.status_code} : {response.json()}")

