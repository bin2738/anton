import requests
from bs4 import BeautifulSoup
import os

def get_2():
    #print("\nПривет! Могу найти тебе подробные данные о компании")
    url = input("\nВведите ссылку:")
    headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
    req =requests.get(url,headers=headers)
    if req.status_code == 200:
        print('Connecting.. ОК 200\n')
        return req.text
    else:
        print('Connecting.. Error')
# Раскрывает все инфу о компании
def parss_2():
    link = get_2()
    soup = BeautifulSoup(link,"html.parser")
    name = soup.find(class_="upper").text
    kart = soup.find(class_="c2m").text
    kontakt = soup.find("span",class_="upper").text
    ifon_2 = soup.find_all("a",class_="nwra lbs64")
    sait = soup.find(class_="sites").text
    
    print(name)
    print(kart)
    print(f"Адрес:{kontakt}")
    tit =[name,kart,kontakt,sait]

    for aifon in ifon_2:
        print(f"Телефон:{aifon.text}")
        tit.append(aifon.text)
        continue  
    print(sait)
    #print(tit)
    save = input("ХОТИТЕ СОХРАНИТЬ ДАННЫЕ (y/n):")
    if save == "y":
        with open(f"/Users/rurikiuan/Desktop/проэкт Антон/data_podro,no/{name}.txt","a") as file:
            file.write(str(tit))
        print(f"Фаил был сохранен\nимя {name} он в папке data")
    else:
        print("Пока")
