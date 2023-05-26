
class New_Class:

    def __init__(self, value=None, next_=None):
        self.value = value
        self.next = next_

    def __str__(self):

        return 'Nope value = ' + str(self.value)

class Linked_List:
    def __init__(self):
        self.first = None
        self.last = None
    def clear(self):
        self.__init__()
    def __str__(self):
        R = ''

        point = self.first
        while point is not None:
            R += str(point.value)
            point = point.next
            if point is not None:
                R += ' '
        return R
    def pushleft(self, value):
        if self.first is None:
            self.first = New_Class(value)
            self.last = self.first

        else:
            new_Nope = New_Class(value, self.first)
            self.first = new_Nope
    def pushright(self,value):
        if self.first is None:
            self.first = New_Class(value)
            self.last = self.first
        else:
            new_Nope = New_Class(value)
            self.last.next = new_Nope
            self.last = new_Nope
    def popleft(self):
        if self.first is None:  # если список пустой, возвращаем None
            return None
        elif self.first == self.last:  # если список содержит только один элемент
            New_Class = self.first  # сохраняем его
            self.__init__()  # очищаем
            return New_Class  # и возвращаем сохраненный элемент
        else:
            New_Class = self.first  # сохраняем первый элемент
            self.first = self.first.next  # меняем указатель на первый элемент
            return New_Class  # возвращаем сохраненный
    def popright(self):
            if self.first is None:  # если список пустой, возвращаем None
                return None
            elif self.first == self.last:  # если список содержит только один элемент
                New_Class = self.first  # сохраняем его
                self.__init__()  # очищаем
                return New_Class  # и возвращаем сохраненный элемент
            else:
                New_Class = self.last  # сохраняем последний
                point = self.first  # создаем указатель
                while point.next is not New_Class:  # пока не найдем предпоследний
                    point = point.next
                point.next = None  # обнуляем указатели, чтобы
                self.last = point  # предпоследний стал последним
                return New_Class  # возвращаем сохраненный
    def __iter__(self):
        self.current = self.first
        return self
    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            self.current = self.current.next
            return New_Class

    def __len__(self): #считаем размер структуры данных
        count = 0
        pointer = self.first
        while pointer is not None:
            count +=1
            pointer = pointer.next
        return count




LL = Linked_List()

LL.pushright(1)
LL.pushleft(2)
LL.pushright(3)
LL.popright()
LL.pushleft(4)
LL.pushright(5)
LL.popleft()

print(LL, 'type: ', type(LL))
print(len(LL))

