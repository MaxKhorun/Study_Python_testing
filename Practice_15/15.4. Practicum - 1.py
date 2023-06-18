"""Напишите программу, которая получает от пользователя имя файла, открывает этот файл в текущем каталоге,
читает его и выводит два слова: наиболее часто встречающееся из тех, что имеют размер более трех символов,
и наиболее длинное слово на английском языке.
"""

eng_alph = "qwertyuiopasdfghjklzxcvbnm"
SIMBOLS = "!@#$%^&*()_+=|?><.,;:'\"\\/{}[]"
"""
    Функция <no_symb(txt):> принимает строку с текстом. Убирает все знаки препинания и возвращает
     текст без символов.
    """
def no_symb(txt):

    for sym in SIMBOLS:
        txt = txt.replace(sym,'')
    return txt.split()

with open(r'D:\SF\test_text_05.05.23.txt', "r", encoding="UTF-8") as f:
     text = f.read().lower()
txt_no_symb = no_symb(text)

wanted_length = int(input('Введите длинну символов для поиска вхождений: '))
output_txt = [it for it in txt_no_symb if len(it) > wanted_length]

'''for i in output_txt:
    if len(i) > wanted_length:
        a = output_txt.count(i)
    a += output_txt.count(i)
print(a)'''

# dictionary solve below
def dict_count_mos(txt):
    count_dict = dict.fromkeys(set(txt), 0)
    for W in txt:
        if len(W) > wanted_length:
            count_dict[W] += 1
    return max(count_dict.items(), key=lambda x:x[1])
def most_often(txt):
    count_items = 0
    list_of_items = []
    for element in output_txt:
        if len(element) > wanted_length:
            temp_count = output_txt.count(element)
            if count_items < temp_count:
                count_items = temp_count
                list_of_items = [element] # REWRITTING!!!! ahahahha)))
            elif count_items == temp_count:
                list_of_items.append(element)
    return list(set(list_of_items))

most_long_W = None
length_of_engWrd = 0
for word in output_txt:
    for letter in word:
        if letter in eng_alph and len(word) > length_of_engWrd:
            length_of_engWrd = len(word)
            most_long_W = [word]
        elif len(word) == length_of_engWrd:
            most_long_W.append(word)


print(f'\nСамое часто встречающееся слово с количестивом знаков '
      f'более указанного значения (слово, кол-во раз): {dict_count_mos(output_txt)};\n'
      f'Самое длинное слово на английском языке: {set(most_long_W)},' f' колличество букв в слове: {len(most_long_W)}')

'''
Ещё один вариант решения: 

def changeText(text):
"""
Функция принимает строку с текстом. 
Убирает все знаки препинания и возвращает
список, состоящий из слов текста.
"""
    for i in '!"\'#$%&()*+-,/:;<=>?@[\\]^_{|}~':
        text = text.replace(i, '')
        
    return text.split()
def mostCommon(text, length = 0):
"""
Функция принимает список и ограничение по длине.
Возвращает самый часто встречающийся элемент.
Если есть несколько элементов с одинаковой самой большой частотой, то вернёт их все.
"""
    most_common = []
    qty_most_common = 0
    
    for item in text:
        if len(item) > length:
            qty = text.count(item)
            if qty > qty_most_common:
                qty_most_common = qty
                most_common = [item]
            elif qty == qty_most_common:
                most_common.append(item)
            
    return list(set(most_common))

def mostLength(text):
"""
Функция принимает список.
Возвращает самый длинный элемент.
Если есть несколько элементов с одинаковой самой большой длиной, то вернёт их все.
"""
    most_length = []
    qty_most_length = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for item in text:
        for char in item:
            if char not in alphabet:
                charEn = False
            else:
                charEn = True
            
        if charEn:
            qty = len(item)
            if qty > qty_most_length:
                qty_most_lenght = qty
                most_lenght = [item]
            elif qty == qty_most_length:
                most_length.append(item)
                
    return list(set(most_length))

nameFile = input('Название файла: ')

with open(nameFile, encoding='utf8') as f:
    fileText = f.read()
    
fileText = changeText(fileText)
print(f'Список самых частых слов длинной более трёх символов: {mostCommon(fileText, 3)}')
print(f'Список самых длинных английских слов: {mostLength(fileText)}')

'''

'''
И ещё один вариант: 



alfE = "qwertyuiopasdfghjklzxcvbnm"
name_file = input("Введите имя файла: ")
SIMBOLS = "!@#$%^&*()_+=|?><.,;'{}[]"
#
with open(name_file, "r", encoding="UTF-8") as f:
    text = f.read().translate({ord(i): None for i in SIMBOLS}).lower().split(" ")

words_set = set(text)
words_dict = dict.fromkeys(words_set, 0)
for word in text:
    if len(word) > 3:
        words_dict[word] += 1
max_elem = max(words_dict.items(), key=lambda x: x[1])

word_len_dict = {}
for word in text:
    word_en = True
    for char in word:
        if char not in alfE:
            word_en = False
            break
    if word_en:
        word_len_dict[word] = len(word)
long_word = max(word_len_dict.items(), key=lambda x: x[1])

print(f"Самое длинное английское слово: {long_word[0]} длина которго {long_word[1]} символов")
print(f"Слово, длинее 3х букв: {max_elem[0]} встречается {max_elem[1]} раз")
'''