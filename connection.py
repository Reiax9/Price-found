import cloudscraper
import csv
from bs4 import BeautifulSoup
from tkinter import *

path = "C:\\Users\\xgarc\\Desktop\\monitor1\\Tiendas\\urls.csv"

#! Create CloudScraper Instance
scraper = cloudscraper.create_scraper() 

#! Bypass antibot to CloudFare
scraper = cloudscraper.create_scraper(
    browser={
        'browser': 'firefox',
        'platform': 'windows',
        'desktop': True,
        'mobile': False,
    }
)

def error_status(url:str) -> None: print(f"No se ha encontrado la página web {url}")

def read_file_urls() -> list:
    with open(path, "r", encoding="utf-8") as file:
        data = csv.reader(file)
        next(data)  #! Salta la primera línea si contiene encabezados
        return list(data)

def search_amazon(r:str, precio:int) -> None:
    precio = 70
    soup = BeautifulSoup(r.text, 'html.parser')
    price_result = soup.find('span', {'class':'a-price-whole'})
    name_result = soup.find(id="productTitle")
    if int(price_result.text.strip().replace(",",'')) <= int(precio): 
        print(f"Esta oferta el {name_result.text.strip()} con el precio de {precio}")

def search_pccomponents(r:str, precio:int) -> None:
    soup = BeautifulSoup(r.text, 'html.parser')
    price_result = soup.find(id="pdp-price-current-integer")
    name_result = soup.find(id="pdp-title")
    if int(price_result.text.strip().rsplit(',')[0]) <= int(precio): 
        print(f"Esta oferta el {name_result.text.strip()} con el precio de {precio}")


def main():
    urls_tiendas = read_file_urls()
    for url, precio in urls_tiendas:
        dominio = url.rsplit("/")[2].replace("www.",'')
        r = scraper.get(url)
        if r.status_code == 200:
            match dominio:
                case "amazon.es"            : search_amazon(r, precio)
                case "pccomponentes.com"    : search_pccomponents(r, precio)
                case _                      : print("El dominio no es de amazon ni de pccomponents")
        else: error_status(url)
             

if __name__ == "__main__":
    main()