import requests
import bs4
import shutil
import os


def get_work(folder, name):
    url = 'http://www.consultingrandomworkgenerator.com/'
    data = get_data_from_url(url)
    save_image(folder, name, data)


def get_data_from_url(url):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    img = soup.find(class_='img-responsive meme')
    img_link = url + img['src']
    img_response = requests.get(img_link, stream=True)

    return img_response.raw


def save_image(folder, name, data):
    file_name = os.path.join(folder, name + '.jpg')
    with open(file_name, 'wb') as fout:
        shutil.copyfileobj(data, fout)