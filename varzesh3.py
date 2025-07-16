import requests
from bs4 import BeautifulSoup
f1=open("flinkfarsi.txt","rt",encoding="utf-8")
s=f1.read()
links=s.strip().split("\n")
for link in links:
    web=requests.get(link)
    soup=BeautifulSoup(web.content)
    dvs=soup.find_all("div",{"class":"news_body_lead"})
    print(dvs)
    img=dvs[0].find_all("img")[0]["src"]
    img_name=img.strip().split("/")[-1]
    f2=open("images1/"+img_name,"wb")
    web=requests.get(img)
    f2.write(web.content)
    f1.close