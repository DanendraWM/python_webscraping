import requests
from bs4 import BeautifulSoup
import csv
hasil = []
page = requests.get(
    'https://www.cnnindonesia.com/search/?query=sepakbola')
data = page.text
soup = BeautifulSoup(data, "html.parser")
find_data = soup.find(
    'div', 'list media_rows middle').findAll('article')
for fn in find_data:
    judul = fn.find('h2', 'title').text
    try:
        kategori = fn.find('span', 'kanal').text
        waktu = fn.find('span', 'date').text
        img = fn.find(
            'span', 'ratiobox ratio_16_9 box_img').find('img')['src']
    except:
        kategori = 'tidak ada kategori'
        waktu = 'tidak ada keterangan'
        img = 'tidak ada gambar'
    hasil.append([judul, kategori, waktu, img])
header = ['judul', 'kategori', 'waktu', 'image']
writer = csv.writer(open('csv/berita_bola_CNN.csv', 'w', newline=''))
writer.writerow(header)
for hsl in hasil:
    writer.writerow(hsl)
