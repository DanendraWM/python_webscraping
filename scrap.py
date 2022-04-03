import requests
from bs4 import BeautifulSoup
import csv

web = 'https://tiket.com/hotel/indonesia/region/jakarta-108001534490276204/page-10'
datas = []
page = requests.get(web)
soup = BeautifulSoup(page.text, 'html.parser')
items = soup.findAll('div', 'hotel-card')
for it in items:
    nama = it.find('h3', 'title ellipsis').text
    alamat = it.find('div', 'location ellipsis').text
    try:
        harga = it.find('div', 'after-price').get_text()
    except:
        harga = 'harga tidak tersedia'
    try:
        rating = it.find('div', 'tiket-impression').get_text()
    except:
        rating = 'tidak ada rating'
    image = it.find('div', 'image-wrap').find('img')['src']
    datas.append([nama, alamat, harga, rating, image])

kepala = ['nama', 'alamat', 'harga', 'rating', 'image url']
writer = csv.writer(open('csv/hotel_jakarta.csv', 'w', newline=''))
writer.writerow(kepala)
for isi in datas:
    writer.writerow(isi)
