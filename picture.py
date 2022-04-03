from unittest import result
from urllib import response
from bs4 import BeautifulSoup
import requests
import os
import random

input_image = input("tag")

response = requests.get(f"https://yande.re/post?tags={input_image}")
soup = BeautifulSoup(response.text, 'html.parser')

root = f'C:\\Users\\hammann\\Pictures\\瑟瑟の圖\\{input_image}'

if not os.path.exists(root):
    os.mkdir(root)
    print(f'資料夾{root}已建立')

result = soup.find_all("span",class_ = "plid")
img_file = []
for n in range(5):
    item = random.choice(result)
    img_file.append(item)
    result.remove(item)
for title in img_file:
    title = title.text[4:]
    name = title[-6:]
    response = requests.get(title)
    soup = BeautifulSoup(response.text, 'html.parser')
    item = soup.find("img",id = "image")
    item = item.get("src")
    if not os.path.exists(root + "\\" + name + ".jpg"):
        img = requests.get(item)
        with open(root + "\\" + name +".jpg ","wb") as file:
            file.write(img.content)
    else:
        print('這張已被下載過')
        continue
print('下載完成')
