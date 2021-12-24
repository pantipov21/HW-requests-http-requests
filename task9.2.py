import sys

sys.path.append("/usr/lib/python3/dist-packages")
import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        print('The task is performing...')
        url = "https://cloud-api.yandex.net:443/v1/disk/resources/upload"
        params = {"path": file_path,
                  "overwrite" : "true"}
        headers = {"Authorization": f'OAuth {self.token}'}

        print('Upload link request is sending...')
        resp = requests.get(url, params=params, headers=headers)
        if (resp.status_code==200):
            print('Upload link received successfully')

            correct_url = resp.json().get('href')

            resp = requests.put(correct_url, data=open(file_path, 'rb'))
            if (resp.status_code == 201):
                print("File uploaded successfully")
            else:
                print(f'Uploading failed. Status code is {resp.status_code}')
        else:
            print(f'Failed to get upload link. Status code is {resp.status_code}')

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'test.txt'
    token = ''

    uploader = YaUploader(token)
    uploader.upload(path_to_file)

