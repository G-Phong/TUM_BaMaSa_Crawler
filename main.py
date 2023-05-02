import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

""" # Set up the options for the Chrome browser to run in headless mode
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')

# Create an instance of the Chrome browser
browser = webdriver.Chrome(options=chrome_options)

# Navigate to the webpage
browser.get('https://fsmb.de/studierende/basama/')

# Wait for the page to fully load (can be adjusted)
browser.implicitly_wait(10)

# Get the page source, which will include the dynamically generated content
page_source = browser.page_source

# Close the browser
browser.quit()

# Use BeautifulSoup to parse the page source
soup = BeautifulSoup(page_source, 'html.parser')

# Extract the relevant content using BeautifulSoup as before
table = soup.find_all('table') 

with open("output.txt", "w", encoding="utf-8") as file:
        file.write(soup.prettify())"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('/path/to/chromedriver') # Pfad zum chromedriver angeben
driver = webdriver.Chrome(service=service)
driver.get('https://fsmb.de/studierende/basama/')

# Warte auf das Laden aller Inhalte (10 Sekunden Timeout)
driver.implicitly_wait(10)

# Extrahiere den HTML-Code
html = driver.page_source

# Schließe den Webbrowser
driver.quit()

# Schreibe den HTML-Code in eine Datei
with open('output2.txt', 'w', encoding='utf-8') as f:
    f.write(html)



""" # URL des zu crawlenden Webs
url = 'https://fsmb.de/studierende/basama/'

# Fordere die Webseite an
response = requests.get(url)

# Überprüfe, ob die Anfrage erfolgreich war
if response.status_code == 200:

    # Feedback Status Code
    print("status code: " + str(response.status_code))

    # Verarbeite die Webseite mit BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    #print(soup.prettify())

    # Tabelle mit Attribut "id" gleich "my-table" finden
    tables = soup.find_all('table')

    with open("output.txt", "w", encoding="utf-8") as file:
        file.write(soup.prettify())


else:
    print('Fehler: Die Anfrage war nicht erfolgreich.') """
