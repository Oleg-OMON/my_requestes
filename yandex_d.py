import os
import requests
from pprint import pprint

token = ' '

class YandexUploader:
    def __init__(self, token):
        self.token = token

    def upload_ph(self, file_list):
        API_YANDEX = "https://cloud-api.yandex.net/"
        headers = {"accept": "application/json", "authorization": f"OAuth {token}"}
        response = requests.get(API_YANDEX + "v1/disk/", headers=headers)
        upload= requests.get(API_YANDEX + 'v1/disk/resources/upload', params={'path':'Files/photo.jpg'}, headers= headers )
        upload_url = upload.json()['href']
        uplaod_photo = requests.put(upload_url, headers= headers, files={'file': open ('photo.jpg', 'rb')})

if __name__ == '__main__':
    my_uploader = YandexUploader('')
    my_uploader.upload_ph(['photo.jpg'])
