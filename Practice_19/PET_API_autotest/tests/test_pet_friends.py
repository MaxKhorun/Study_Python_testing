from ..api_catalog import PetFriends
from ..settings import login_email, login_pass

pf = PetFriends()

def test_api_key_for_valid_user(email=login_email, passw=login_pass):
    status, result = pf.get_api_key(email, passw)
    assert status == 200
    assert 'key' in result

# def test_get_petlist_wth_auth_key(filter=''):
#     _, auth_key = pf.get_api_key(login_email, login_pass)
#     status, result = pf.get_list_of_pets(auth_key, filter)
#     assert status == 200
#     assert len(result['pets']) > 0
#
#     '''[POST] / api / pets — добавление информации о новом питомце;'''
# def test_post_new_pet(name='Vitek', pet_type='Canary', photo_url='no_photo'):
#     status, result = pf.post_newPet(name, pet_type, photo_url)
#     assert status == 200
#     assert 'Vitek' in result

    # '''[DELETE] / api / pets / {pet_id} — удаление питомца из базы данных;'''


    # '''[PUT] / api / pets / {pet_id} — обновление информации о питомце.'''