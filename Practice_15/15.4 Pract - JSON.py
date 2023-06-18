import json

with open(r'D:\SF\JSON_example.txt', 'r', encoding="utf8") as f:
    n_d = json.load(f)

list_of_check_it = {
'timestamp': int,
'referer': 'url',
'location': 'url',
'remoteHost': str,
'partyId': str,
'sessionId': str,
'pageViewId': str,
'eventType': str, # (itemBuyEvent или itemViewEvent)
'item_id': str,
'item_price': int,
'item_url': 'url',
'basket_price': str,
'detectedDuplicate': bool,
'detectedCorruption': bool,
'firstInSession': bool,
'userAgentName': str,
}

def check(item):
    return isinstance(item, int)

print(check('timestamp'))



# print(check(list_of_check_it[0]))

# Dict_1 = {key:value
#           for key,value in data_f_check, }
# print(Dict_1)
# print(data_f_check,'\n',
#       type(data_f_check))

# with open(r'C:\test\test.json', 'r') as f:
#     json_data = json.load(f)
#
# print(json.dumps(json_data, indent=2))