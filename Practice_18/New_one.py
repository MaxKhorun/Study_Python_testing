import requests
import json

'''# r = requests.get('https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=html')
# r_1 = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
r_2 = requests.get('https://api.github.com')
answ_txt = json.loads(r_2.content)
print(type(answ_txt))
# print(r_1.content)
print(answ_txt['following_url'])
# for t in answ_txt:
#     print(answ_txt[:50], '\n')
data = {'key':'value'}
r_2 = requests.post('https://httpbin.org/post', json = json.dumps(data))
print(r_2.content)
'''

get_txt = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
mod_get_txt = json.loads(get_txt.content)
# print(mod_get_txt)

# answ_1 = open('test_JSON_answer_01.06.txt', 'w')
print(mod_get_txt[0])
# answ_1.write(str(mod_get_txt))