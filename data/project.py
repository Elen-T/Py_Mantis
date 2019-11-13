import random
import string
from model.project import Project

def random_string(prefix,maxlen): #генерация случайных тест данных (prefix - слово с кот начинается строка,maxlen - мах длинна строки )
    symbols=string.ascii_letters + string.digits + " " # это символы которые будут в случайно сгенерированной строке
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen)) ]) # random.choice случайным образом выбирает символ из строки случайной длинны - random.randrange(maxlen) (будет сгенерир случайн длинна не превыш мах) потом склеиваем этот список -"".join


testdata =[Project(name=random_string("name",10), status=random_string("1",20) , description=random_string("description",20) )
    for i in range(1)]# будет сгенерирован объект Group, содержащийслучайные данные, 5 раз и из этих сгенерированных объектов будет построен список

