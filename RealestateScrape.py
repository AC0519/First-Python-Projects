import requests
from bs4 import BeautifulSoup

r=requests.get("https://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s=0.html")
c=r.content

soup=BeautifulSoup(c,"html.parser")


all=soup.find_all("div",{"class":"propertyRow"})


#all[0].find("h4", {"class","propPrice"}).text.replace("\n","").replace("$","").replace(",","")

l=[]
for item in all:
    d={}
    d["Price"]=item.find("h4", {"class","propPrice"}).text.replace("\n","").replace("$","").replace(",","")
    d["Address"]=item.find_all("span",{"class":"propAddressCollapse"})[0].text
    d["Locality"]=item.find_all("span",{"class":"propAddressCollapse"})[1].text
    try:
        d["Beds"]=item.find("span",{"class":"infoBed"}).find("b").text
    except:
        d["Beds"]=None

    try:
        d["SqFt"]=item.find("span",{"class":"infoSqFt"}).find("b").text
    except:
        d["SqFt"]=None

    try:
        d["Full Baths"]=item.find("span",{"class":"infoValueFullBath"}).find("b").text
    except:
        d["Full Baths"]=None

    try:
        d["Half Baths"]=item.find("span",{"class":"infoValueHalfBath"}).find("b").text
    except:
        d["Full Baths"]=None

    for column_group in item.find_all("div",{"class":"columnGroup"}):
        for feature_group, feature_name in zip(column_group.find_all("span",{"class":"featureGroup"}),column_group.find_all("span",{"class":"featureName"})):
            if "Lot Size" in feature_group.text:
                d["Lot Size"]=feature_name.text
    l.append(d)

import pandas
df=pandas.DataFrame(l)
df.to_csv("Realestate.csv")
