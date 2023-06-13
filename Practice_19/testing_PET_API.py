import requests
status = 'available'
base_url = 'petstore.swagger.io/v2'
resp = requests.get(f'https://{base_url}/pet/findByStatus?status={status}', headers = {'accept': 'application/json'})
resp_mod = resp.json()
print(resp_mod)

id_pet = 9223372036854635244

resp_getPet = requests.get(f'https://{base_url}/pet/{id_pet}')
print(resp_getPet.json())

post_params = {
    'name': 'Lucky Bastard',
    'photoUrls': 'no photo',
    'status': 'available'
}
resp_postPet = requests.post(f'https://{base_url}/pet?{post_params}')
print(resp_postPet.json())