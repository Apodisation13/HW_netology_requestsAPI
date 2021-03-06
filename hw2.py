import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загруджает файл file_path на яндекс диск"""

        response = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload',
                                params={'path': file_path},
                                headers={'Authorization': f'OAuth {self.token}'})
        # print(response.status_code)
        if response.status_code == 200:
            print("Успешно получена ссылка для загрузки файла")
            href = response.json()['href']
            # print(href)
            with open(f'{"D:/" + file_path}', 'rb') as f:
                r = requests.put(href, files={'file': f})
            if r.status_code == 201:
                return print("Успешная загрузка")
            return print(f"Упс, похоже что-то пошло не так. Ошибка {r.status_code}")
        return print(f'Ошибка получения ссылки для загрузки файла {response.status_code}')


if __name__ == '__main__':
    token = "mytoken"
    file = 'maxresdefault.jpg'  # чисто название файла
    uploader = YaUploader(token)
    uploader.upload(file)
