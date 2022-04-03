from logging import root
from tkinter import image_names
from turtle import title
from unittest import result
from urllib import response
from bs4 import BeautifulSoup
import requests
import os
while True:
    
    input_image = input("車號")

    if input_image == 'stop':
        print('程式結束')
        break
    
    response = requests.get(f"https://nhentai.net/g/{input_image}/")
    soup = BeautifulSoup(response.text, 'html.parser')

    results = soup.find_all("img",class_="lazyload")

    title = soup.find("span",class_="pretty")
    title = str(title.text)
    title = title.replace(" ", "_")
    title = title.replace("?", "")
    
    long = [result.get("data-src") for result in results]
    long = long[1:-5]
    long = len(long)

    root = f"C:\\Users\\hammann\\Pictures\\R18\\{title}"
    if not os.path.exists(root):
        os.mkdir(root)
        print('資料夾建立')
    else:
        print('載過了喔還想瑟瑟阿')
        continue

    print(f"下載開始 pages:{long:3d}")
    print('Page')
    for i in range(1,long+1):
        response = requests.get(f"https://nhentai.net/g/{input_image}/{i}/")
        soup = BeautifulSoup(response.text, 'html.parser')

        pic = soup.find_all("img")    
        pic = pic[1]
        pic = pic.get("src")
        img = requests.get(pic)
        with open(root +"\\"+ str(i) + ".jpg", "wb") as file:
            file.write(img.content)
        print(f'{i:3d}')

    print('has been download')