import requests
from bs4 import BeautifulSoup
import pandas as pd

TitleName=[] 
Gross=[] 
Weekend=[]
Week=[]

url = "https://www.imdb.com/chart/boxoffice/?ref_=nv_ch_cht"
r = requests.get(url).content
soup = BeautifulSoup(r, "html.parser") 
list = soup.find("tbody", {"class":""}).find_all("tr")
x = 1
for i in list:
    title = i.find("td",{"class":"titleColumn"})
    gross = i.find("span",{"class":"secondaryInfo"})
    weekend = i.find("td",{"class":"ratingColumn"})
    week=i.find("td",{"class":"weeksColumn"})
    
    TitleName.append(title.text) 
    Gross.append(gross.text)
    Weekend.append(weekend.text)
    Week.append(week.text)

df=pd.DataFrame({'Movie Title' : TitleName,'Weekend ':Weekend,'Gross':Gross,'Week':Week})
df.to_csv('DS-PR1-18IT012.csv', index=False, encoding='utf-8')