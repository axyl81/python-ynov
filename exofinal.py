import requests
from bs4 import BeautifulSoup


rss_url = 'https://www.lemonde.fr/rss/une.xml'


response = requests.get(rss_url)
soup = BeautifulSoup(response.text, 'xml')


def get_domain(url):
    
    domain = url.split('//')[1].split('/')[0]
    return domain


def get_page_title(url):
    page_response = requests.get(url)
    page_soup = BeautifulSoup(page_response.text, 'html.parser')
    title_tag = page_soup.find('title')
    return title_tag.text if title_tag else 'N/A'


article_number = 1

for entry in soup.find_all('item'):
    title = entry.title.text
    link = entry.link.text
    category = entry.category.text if entry.category else 'Aucune catégorie'
    domain = get_domain(link)
    page_title = get_page_title(link)

    
    description = entry.description.text if entry.description else 'Aucun texte'

  

    print(f"Article numéro {article_number}")
    print(f"Texte important : {description}")
    print(f"URL : {link}")
    print(f"Domaine : {domain}")
    print(f"Catégorie : {category}")
    print(f"Titre de l'article : {title}")
    print(f"Titre de la page : {page_title}\n")
    
   
    
    
    article_number += 1
