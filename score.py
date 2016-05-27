from bs4 import BeautifulSoup 
import urllib2
import os
import time
from gi.repository import Notify


url="https://cricket.yahoo.com/cricket-live-score-england-vs-sri-lanka_192397"
#url="https://cricket.yahoo.com/cricket-live-score-england-vs-sri-lanka_192397"
url="https://cricket.yahoo.com/cricket-live-score-gujarat-lions-vs-hyderabad_193923"
page=urllib2.urlopen(url)
soup = BeautifulSoup(page.read(),'html.parser')
#print(soup.prettify())
print "now for current ongoing match "

while(1):
    info= " "
    infohead=" "
    for name in soup.find_all(class_="team-name",limit=2):
        infohead= infohead+ name.get_text() + " "
    for name in soup.find_all(class_='name',limit=1):
        print(name.get_text())
        info =info + name.get_text()
    for res in soup.find_all(class_='result',limit=1):
        print(res.get_text())
        info = info + res.get_text()
    for mom in soup.find_all(class_='sn',limit=1):
        print(mom.get_text())
        info = info + "\n MOM: "+ mom.get_text()




    i=0
    sctmlst=[" "," "," "," "," "," "," "]
    for team in soup.find_all(class_='tname',limit=2):
        sctmlst[i]= team.get_text()
        i= i+1
        print(team.get_text())
    
    for score in soup.find_all(class_='score',limit=2):
        sctmlst[i]= score.get_text()
        i= i+1
        print(score.get_text())

    for score in soup.find_all(class_='scr',limit=2):
        sctmlst[i]= score.get_text()
        i= i+1

    for ovr in soup.find_all(class_='ings-overs',limit=2):
        sctmlst[i]= ovr.get_text()
        sctmlst[i]= "overs completed: "+sctmlst[i]
        i= i+1
    for rrr in soup.find_all(class_='rrr',limit=1):
        sctmlst[i]= rrr.get_text()
        sctmlst[i]= "reqd run rate: "+sctmlst[i]
        i= i+1


    info= info + sctmlst[0]+" "+ sctmlst[2]+ " " + sctmlst[1]+" " + sctmlst[3]+ " "+ sctmlst[4]+ " "+ sctmlst[5]
    
    Notify.init("Hello world")
    Hello=Notify.Notification.new(infohead, info , "dialog-information")
    Hello.show()

    time.sleep(200)
