import requests
from bs4 import BeautifulSoup
import os


# Подключение\\\
def get_url(val,page=False):
    url = f"https://www.list-org.com/search?type=all&val={val}&page={page}"
    headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
    params = {"val":val,"page":page}
    req = requests.get(url,headers=headers,params=params)
    if req.status_code == 200:
        print('Connecting.. ОК\n')
        return req.text
    else:
        print('Connecting.. Error')
# Ищет по запросу данные\\\
def passr(val,page=False):
    link = get_url(val,page)
    soup = BeautifulSoup(link, "html.parser")
    a_text_p = soup.find(class_="content").find("p").text
    print(f"{a_text_p} По запросу '{val}'\n")
    ooo = []
    coint = 0
    for b_href in soup.find(class_="org_list").find_all("a"):
        ab_text = b_href.text
        print(f"({coint})-{ab_text}")
        ab_href="https://www.list-org.com"+b_href.get("href")
        coint +=1
        print(ab_href)
        print("\n")
        ooo.append(f"({coint})-{ab_text}//{ab_href}")
    # Записывает всю выдачу\\\  
    #with open(f"/Users/rurikiuan/Desktop/проэкт Антон/data/ООО-ИП{val}.txt","a") as fi:
           # fi.write(str(ooo))   


    

