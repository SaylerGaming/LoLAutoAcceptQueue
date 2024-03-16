import requests
from os.path import exists

def create(filename: str, url: str) -> None:
    if not exists('./src/'+filename):
        img_data = requests.get(url).content
        with open(filename, 'wb') as handler:
            handler.write(img_data)

def doesImagesExists() -> bool:
    return exists('./src/acceptQueue.png') and exists('./src/acceptQueue.png')

if __name__ == '__main__':
    create('./src/button.png', 'https://i.ibb.co.com/vZYKXcx/button.png')
    create('./src/inQueue.png', 'https://i.ibb.co.com/hfq4r1Q/inQueue.png')
