

G_1 = {
'Спасская': {"Садовая": 2, "Сенная пл.": 3, "Достоевская": 5},
"Садовая": {"Сенная пл.": 2, "Спасская": 2, "Адмиралтейская": 5, "Звенигородская": 7},
"Сенная пл.": {"Садовая": 2, "Спасская": 3},
"Достоевская": {"Владимирская": 2, "Спасская": 6},
"Владимирская": {"Достоевская": 2, "Пушкинская": 5},
"Пушкинская": {"Звенигородская": 2, "Владимирская": 5},
"Звенигородская": {"Пушкинская": 2, "Садовая": 6},
"Адмиралтейская": {"Садовая": 4}
}

D = {k: 100 for k in G_1.keys()}

start_point = "Адмиралтейская"
D[start_point] = 0

check_dict = {k: False for k in G_1.keys()} #словарь с булевыми значениями для проверки точек

for m_d in range(len(D)): # "Эта конструкция нужна для определения минимального времени"
    min_dist = min([k for k in check_dict.keys() if not check_dict[k]], key=lambda x: D[x])

    for val_pick in G_1[min_dist].keys():
        D[val_pick] = min(D[val_pick], D[min_dist] + G_1[min_dist][val_pick])
    check_dict[min_dist] = True

print(D)






