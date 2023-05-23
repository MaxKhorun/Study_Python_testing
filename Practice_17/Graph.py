import gettext

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

'''D = {k: 100 for k in G_1.keys()}

start_point = "Адмиралтейская"
D[start_point] = 0

check_dict = {k: False for k in G_1.keys()} #словарь с булевыми значениями для проверки точек
P = {k: None for k in G_1.keys()}


for m_d in range(len(D)): # "Эта конструкция нужна для определения минимального времени"
    min_dist = min([k for k in check_dict.keys() if not check_dict[k]], key=lambda x: D[x])

    for val_pick in G_1[min_dist].keys():
        if D[val_pick] > D[min_dist] + G_1[min_dist][val_pick]:
            D[val_pick] = D[min_dist] + G_1[min_dist][val_pick]
            P[val_pick] = min_dist
            # print(G_1[min_dist][val_pick])

        # D[val_pick] = min(D[val_pick], D[min_dist] + G_1[min_dist][val_pick])
    check_dict[min_dist] = True
print(D[min_dist], '\n---', D[min_dist] + G_1[min_dist][val_pick])


print(D)'''



# Trees

class Bin_Trees:
    def __init__









'''def insert_left(self, next_value):
    if self.left_child is None:
        self.left_child = Bin_Trees(next_value)

    else:
        new_child = Bin_Trees(next_value)
        new_child.left_child = self.left_child
        self.left_child = new_child
    return self



def in_order(self):
    if self.left_child is not None: # если левый потомок существует
        self.left_child.in_order() # рекурсивно вызываем функцию

    print(self.value) # процедура обработки

    if self.right_child is not None: # если правый потомок существует
        self.right_child.in_order() # рекурсивно вызываем функцию


def post_order(self):
    if self.left_child is not None: # если левый потомок существует
        self.left_child.post_order() # рекурсивно вызываем функцию

    if self.right_child is not None: # если правый потомок существует
        self.right_child.post_order() # рекурсивно вызываем функцию

    print(self.value) # процедура обработки


def pre_order(self):
    print(self.value) # процедура обработки

    if self.left_child is not None: # если левый потомок существует
        self.left_child.pre_order() # рекурсивно вызываем функцию

    if self.right_child is not None: # если правый потомок существует
        self.right_child.pre_order() # рекурсивно вызываем функцию

print()'''