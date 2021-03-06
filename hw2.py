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
        href = response.json()['href']
        # print(href)
        with open(f'{"D:/" + file_path}', 'rb') as f:
            r = requests.put(href, files={'file': f})
        if r.status_code == 201:
            return print("Успешная загрузка")
        return print(f"Упс, похоже что-то пошло не так. Ошибка {r.status_code}")


if __name__ == '__main__':
    token = "AgAAAAA854AuAADLWyTnygif80QiiTab_zpBVtM"
    file = 'maxresdefault.jpg'  # чисто название файла
    uploader = YaUploader(token)
    uploader.upload(file)
