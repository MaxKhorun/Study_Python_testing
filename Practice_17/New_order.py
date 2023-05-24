
class Nope:

    def __init__(self, value = None, next_ = None):
        self.value = value
        self.next_ = next_

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
            self.first = Nope(value)
            self.last - self.first

        else:
            new_Nope = Nope(value, self.first)
            self.first = new_Nope

    def pushright(self,value):
        if self.first is None:
            self.first = Nope(value)
            self.last = self.first
        else:
            new_Nope = Nope(value, self.first)
            self.first = new_Nope

    def popleft(self):
        if self.first is None:  # если список пустой, возвращаем None
            return None
        elif self.first == self.last:  # если список содержит только один элемент
            Nope = self.first  # сохраняем его
            self.__init__()  # очищаем
            return Nope  # и возвращаем сохраненный элемент
        else:
            Nope = self.first  # сохраняем первый элемент
            self.first = self.first.next  # меняем указатель на первый элемент
            return Nope  # возвращаем сохраненный

    def popright(self):
            if self.first is None:  # если список пустой, возвращаем None
                return None
            elif self.first == self.last:  # если список содержит только один элемент
                Nope = self.first  # сохраняем его
                self.__init__()  # очищаем
                return Nope  # и возвращаем сохраненный элемент
            else:
                Nope = self.last  # сохраняем последний
                pointer = self.first  # создаем указатель
                while pointer.next is not Nope:  # пока не найдем предпоследний
                    pointer = pointer.next
                pointer.next = None  # обнуляем указатели, чтобы
                self.last = pointer  # предпоследний стал последним
                return Nope  # возвращаем сохраненный

LL = Linked_List()

LL.pushright(1)
LL.pushleft(2)
LL.pushright(3)
LL.popright()
LL.pushleft(4)
LL.pushright(5)
LL.popleft()

print(LL)

