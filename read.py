import urllib.request
from bs4 import BeautifulSoup




url = "http://www.overraskelse.no/fullkorn?fkid="



file = open("t.txt","w")
for i in range(1,662):
    page = urllib.request.urlopen(url+str(i))
    soup = BeautifulSoup(page, 'html.parser')
    fullkorn = soup.find("div", {"id": "fullkornTekstView"}).text.strip()
    ettertanke = soup.find("div", {"id": "fullkornEttertankeView"}).text.strip()

    skriv = fullkorn + '\n' +ettertanke +'\n' 
    file.write(skriv)

    
file.close();

   
#fullkornTekstView
#fullkornEttertankeView
