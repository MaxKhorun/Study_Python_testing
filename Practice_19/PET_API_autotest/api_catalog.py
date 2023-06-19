import requests
import json

class PetFriends:
    def __init__(self):
        self.base_url = 'petstore.swagger.io/v2'

    def get_api_key(self, email: str, password: str) -> json:
        """Метод отправляет запрос к API; возвращает статус и результата в установленных переменных 
        в формате json с уникальным ключом пользователя, найденным по отправленным email и password"""

        headers = {
            'email' : email,
            'password' : password
        }
        res = requests.get(self.base_url+'/api/key', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result
    def get_list_of_pets(self, auth_key: str, filter: str) -> json:
        """Метод отправляет завпрос к API с ключом пользователя и возварщает спсиок питомцев с учётом
        параметров filter"""
        header = {'auth_key': auth_key['key']}
        filter = {'filter': filter}
        res = requests.get(self.base_url+'/api/pets', headers=header, params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result
    def post_newPet(self, name, pet_type, photo_url):

        headers ={
            'accept' : 'application/json',
            'Content-Type' : 'application/json'
        }
        data = {
            'name': name,
            'category': {'name': pet_type},
            'photoUrls': photo_url
        }

        #pet_photo = r"C:\Users\M.Kh\PycharmProjects\Study_Python_testing\Practice_19\PET_API_autotest\tests\images\kenar-vitek.jpg"
        #photo_file = {'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')}

        res = requests.post(self.base_url+'/pet', headers= headers, data= data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result