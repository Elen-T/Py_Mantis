from sys import maxsize

class Project:
    def __init__ (self, name=None, status=None, description=None, id=None):
        self.name = name
        self.status = status
        self.description = description
        self.id = id

    def __repr__(self): #спец функция, определяет как будет выглядеть объект при выводе на консоль
        return "%s:%s:%s:%s" % (self.id, self.name, self.status,self.description)

    def __eq__(self, other): # сравнение текущего обьекта с новым other
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name #  группы равны если совпадают имена, и также совпад ид либо у одной из них неопределен

    # вычисление по группе ключа используемого для сравнения
    def id_or_max(self):
        if self.id:
            return int(self.id)  # если есть ид , то возвращается он
        else:
            return maxsize     # если нет ид , то возвращается мах число