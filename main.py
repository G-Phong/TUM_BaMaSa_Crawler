import requests
from bs4 import BeautifulSoup

# URL des zu crawlenden Webs
url = 'https://www.example.com'

# Fordere die Webseite an
response = requests.get(url)

# Überprüfe, ob die Anfrage erfolgreich war
if response.status_code == 200:
    # Verarbeite die Webseite mit BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Hier kann dein Crawler-Code eingefügt werden
else:
    print('Fehler: Die Anfrage war nicht erfolgreich.')
