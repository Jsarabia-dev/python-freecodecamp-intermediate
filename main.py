import sys
from timeit import default_timer as timer
from loguru import logger

from collections import Counter, namedtuple, OrderedDict, defaultdict, deque
from itertools import *
from functools import *
import operator

from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
import logging
import logging.config
import traceback
import time
import json
import random
import numpy as np
logger.add(sys.stderr, format="{time} {level} {message}", filter="python-intermediate", level="INFO")


def separator(message: str):
    logger.info("\n")
    logger.info(message)


def separator_line():
    logger.info("========================================================")


def mainList():
    # List: Ordered, inmutable, allows duplicated elments
    myList = [1, 2, 3, 4, 5, 6]
    myList_two = [i + i for i in myList]

    myList = [{"a": "b"}, {"a": "c"}]
    print(myList)
    print(myList_two)


def mainTuples():
    # Tuple: Ordered, inmutable, allows duplicated elments
    tupleOne = "value1", 2, True, "value4"
    tupleWithOneElment = "value1",
    print(tupleOne)
    print(tupleWithOneElment)

    tupleOne = tuple(["value1", 2, True, "value4"])  # Other way
    print(tupleOne)
    item = tupleOne[0]  # Access in tuple
    # tupleOne[0] = "new value error"  - Error immutable tuples
    lastItem = tupleOne[-1]  # Las item
    print(item)
    print(lastItem)
    print()

    #  Iterate tuples
    for item in tupleOne:
        print(item)
    print()

    # If element exist in tuple
    if "value4" in tupleOne:
        print(f"Value4 found")
    else:
        print("No Founded")
    print()

    tupleOne = ("a", "p", "p", "l", "e")
    print(tupleOne.count("p"))
    print(tupleOne.index("p"))  # First match index
    print()

    # Cast tuple to List and List to Tuple
    my_list = list(tupleOne)
    print(f"{my_list} - {type(my_list)}")
    tupleTwo = tuple(my_list)
    print(f"{tupleTwo} - {type(tupleTwo)}")
    print()

    tupleOne = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(tupleOne)
    tupleTwo = tupleOne[::-1]  # Reverse tuple
    print(tupleTwo)
    print()

    # Destructuring
    tupleOne = "value1", 20, True, "value4"
    name, age, is_adult, adress = tupleOne
    print(f'{name} - {age} - {is_adult} - {adress}')


def mainDict():
    # Dictionaries: Key-value pairs, Unordered, Mutable
    # Form 1
    myDict = {"name": "max", "age": 2, "city": "New york"}
    print(myDict)

    # Form 2
    myDict2 = dict(name="Max", age=2, city="New york")
    print(myDict)

    # Get value
    value = myDict2["name"]
    print(value)

    # Put or override value
    myDict2["email"] = "email@gmail.com"
    print(myDict2)

    # Delete value - del, pop,
    del myDict2["email"]
    print(myDict2)

    if "name" in myDict2:
        print(myDict2["name"])

    print("\nKEYS")
    for key in myDict2:
        print(key)

    print("\nVALUES")
    for value in myDict2.values():
        print(value)

    print("\nKEY - VALUES")
    for key, value in myDict2.items():
        print(key, ":", value)

    print("\n DICT UPDATE")
    myDict = {"name": "max", "age": 2, "city": "New york"}
    myDict2 = dict(name="Max", age=2, city="New york", new_key="new value")
    myDict.update(myDict2)
    print(myDict)

    print("\n OTHER IMMUTABLE KEY - VALUES")
    my_tuple = (2, 1)
    my_tuple2 = ("cat2", 2)
    my_dict = {my_tuple: [{"a": "b"}, {"a": "b"}], my_tuple2: [{"a": "b"}]}

    print(type(my_dict.get(my_tuple)))
    my_dict.get(my_tuple).append({"a": "b"})
    print(my_dict)


def mainSet():
    # Sets: unordered, mutable, no duplicates
    my_set = {1, 2, 3, 1, 3}
    print(my_set)

    my_set = set("Hello")
    print("\n", my_set)

    my_set.add(1)
    my_set.add(2)
    my_set.add(3)
    print("\n my_set.add: ", my_set)

    my_set.remove(2)
    # my_set.remove(4) # ERROR - If no exist throw KeyError
    print("\n my_set.remove(2): ", my_set)

    my_set.discard(2)  # If not exist no throw error
    my_set.discard(3)
    print("\n my_set.discard(2 and 3): ", my_set)

    print("\n my_set.pop(): ", my_set.pop())  # Remove and Return arbitrary element
    print("\n befor my_set.pop(): ", my_set)

    separator("Iterate my_set")
    for i in my_set:
        logger.info(i)

    logger.info(my_set)

    separator("unions my_set")
    odds = {1, 3, 5, 7, 9}
    evens = {0, 2, 4, 6, 8}
    primes = {2, 3, 5, 7}

    u = odds.union(evens)
    logger.info(u)

    i = odds.intersection(primes)  # Retorna los elementos duplicados
    logger.info(i)

    separator("differences sets")
    setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    setB = {1, 2, 3, 10, 11, 12}
    logger.info("setA: {}", setA)
    logger.info("setB: {}", setB)
    logger.info(setA.difference(setB))  # Diferencias solo del setA

    separator("symetric differences sets")
    logger.info(setA.symmetric_difference(setB))  # Diferencias de ambos

    separator("update setA")
    setA.update(setB)
    logger.info("setA: {}", setA)

    separator("difference_update setA")
    setA.difference_update(setB)  # Elimina en setA los elementos que hacen match con setB
    logger.info("setA: {}", setA)

    separator("symmetric_difference_update setA")
    setA.symmetric_difference_update(
        setB)  # Agrega los elementos diferentes de ambos, NO agrega lo que estan duplicados en ambos
    logger.info("setA: {}", setA)

    separator("issubset setB")
    setA = {1, 2, 3, 4, 5, 6}
    setB = {1, 2, 3}
    logger.info("setB.issubset: {}", setB.issubset(
        setA))  # Valida si setB es un subset de setA, tienen que matchear TODOS los valores de setB
    logger.info("setB.issuperset: {}",
                setB.issuperset(setA))  # Lo contrario, valida si el setB tiene TODOS los valores del setA

    separator("isdisjoin setB")
    setA = {1, 2, 3, 4, 5, 6}
    setB = {1, 2, 3}
    setC = {4, 5, 6}
    logger.info("setB.isdisjoin: {}", setB.isdisjoint(setC))  # Valida si NO existen elementos duplicados

    separator("Copy sets")
    setA = {1, 2, 3, 4, 5, 6}
    setB = set(setA)
    setA.add(7)
    logger.info("setB: {}", setB)
    logger.info("setA: {}", setA)


def mainString():
    # Strings: ordered, inmutable, text representation
    my_string = """wena 
            I´am
    lineas1
    l2"""

    logger.info(my_string)

    my_string = "Hello World"
    char = my_string[0]
    sub_string = my_string[1:]
    logger.info(char)
    logger.info("sub_string: {}", sub_string)
    logger.info("todos los char: {}", my_string[::1])
    logger.info("todos los segundos char: {}", my_string[::2])
    logger.info("string invertido: {}", my_string[::-1])

    separator("Recorrer String")
    for s in my_string:
        logger.info(s)

    char = "e"
    separator("if char in string")
    if char in my_string:
        logger.info("is {}", char)
    else:
        logger.info("not {}", char)

    my_string = "     Hello World    "
    logger.info("my_string.strip {}", my_string.strip())

    separator("string startwith")
    my_string = "Hello World"
    logger.info("my_string.startswith('Hel'): {}", my_string.startswith('Hel'))

    separator("string endwith")
    my_string = "Hello World"
    logger.info("my_string.endswith('rld'): {}", my_string.endswith('rld'))

    separator("string find")
    my_string = "Hello World"
    logger.info("my_string.find('rld'): {}", my_string.find('l'))  # Retorna el primer index encontrado
    logger.info("my_string.count('l'): {}", my_string.count('l'))

    separator("string to list")
    my_string = "Hello World Bro"
    my_list = my_string.split()
    logger.info("my_list: {}", my_list)

    my_string = "Hello,World,Bro"
    my_list_comma = my_string.split(",")
    logger.info("my_list_comma: {}", my_list_comma)

    my_list_join = ', '.join(my_list_comma)
    logger.info("my_list_join: {}", my_list_join)

    my_list_mult = ['ja'] * 100
    logger.info("my_list_mult: {}", my_list_mult)

    separator("my_string_sum - bad - expensive")
    start = timer()
    my_string_sum = ''
    for s in my_list_mult:
        my_string_sum += s
    stop = timer()
    logger.info("my_string_sum: {}", my_string_sum)
    logger.info("time: {}", stop - start)

    separator("my_string_sum good")
    start = timer()
    my_string_sum = ''.join(my_list_mult)
    stop = timer()
    logger.info("my_string_sum: {}", my_string_sum)
    logger.info("time: {}", stop - start)


def mainCollections():
    # collections: Counter, namedtuple, OrderedDict, defautldict, deque
    a = "aaaaabbbbccc"
    my_counter = Counter(a)
    logger.info("my_counter: {}", my_counter)
    logger.info("my_counter.most_common(1): {}", my_counter.most_common(1))  # Trae el primer elemento mas repetido
    logger.info(" my_counter.most_common(1)[0][0]: {}",
                my_counter.most_common(1)[0][0])  # Traer la 1a key del 1er elemento

    separator("my_counter to list")
    logger.info("list(my_counter.elements()): {}", list(my_counter.elements()))

    separator("named_tuple")
    Point = namedtuple('Point', 'x, y')
    pt = Point(1, -4)
    logger.info("pt = Point(1, -4): {}", pt)
    logger.info("pt.x: {}, pt.y: {}", pt.x, pt.y)

    separator(
        "OrderedDict")  # Similar a los diccionaros, pero este recuerda el orden en que fueron insertados los datos
    ordered_dict = OrderedDict()
    ordered_dict['a'] = 123
    ordered_dict['v'] = 1
    ordered_dict['default_dict'] = 9
    ordered_dict['i'] = 0
    logger.info("ordered_dict: {}", ordered_dict)

    separator(
        "DefautlDict")  # Igual a un dict con la diferencia de que tienes "keys" con valores por "defecto" si aun no han sido seteadas
    default_dict = defaultdict(int)
    default_dict['a'] = 1
    default_dict['b'] = 2
    logger.info("default_dict: {}", default_dict)
    logger.info("default_dict['a']: {}", default_dict['a'])
    logger.info("default_dict['b']: {}", default_dict['b'])
    logger.info("default_dict['c'] -> devuelve el valor por defecto del tipo de var (int = 0): {}", default_dict['c'])

    separator("deque")  # Una cola que puede agregar y quitar de ambos extremos
    my_deque = deque()
    my_deque.append(1)
    my_deque.append(2)
    logger.info("my_deque: {}", my_deque)

    separator_line()
    my_deque.appendleft(0)
    logger.info("my_deque.appendleft(0): {}", my_deque)

    separator_line()
    logger.info("my_deque.pop(): {}", my_deque.pop())
    logger.info("my_deque: {}", my_deque)

    separator_line()
    logger.info("my_deque.popleft(): {}", my_deque.popleft())
    logger.info("my_deque: {}", my_deque)

    separator_line()
    my_deque.clear()
    logger.info("my_deque.clear(): {}", my_deque)

    separator_line()
    my_deque = deque()
    my_deque.append(1)
    my_deque.append(2)
    my_deque.extend([3, 4, 5, 6])

    logger.info(" my_deque.extend: {}", my_deque)
    my_deque.extendleft([0, -1, -2])

    logger.info(" my_deque.extendleft: {}", my_deque)

    my_deque.rotate(1)  # Avanza en 1 la posiciones de la dequee
    logger.info("my_deque.rotate(1): {}", my_deque)

    my_deque.rotate(-1)  # Retrocede en 1 a la izquierda
    logger.info("my_deque.rotate(1): {}", my_deque)


def mainItertools():
    # itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators
    separator_line()
    logger.info(" ### ITERTOOLS ###")

    separator("PRODUCT")  # Repite todas las posibilidades
    a = [1, 2]
    b = [3, 4]
    prod = product(a, b)
    logger.info("prod: {}", prod)
    logger.info("list(prod): {}", list(prod))

    separator_line()
    logger.info("product repeat 2")
    a = [1, 2]
    b = [3]
    prod = product(a, b, repeat=2)
    logger.info("list(product(a, b, repeat=2)): {}", list(prod))

    separator("PERMUTATIONS")  # Retorna todos los posibles ordenamientos
    a = [1, 2, 3]
    perm = permutations(a)
    logger.info("list(perm): {}", list(perm))

    separator("COMBINATIONS")  # Retorna todos los COMBINACIONES posibles entregandoles un length
    a = [1, 2, 3, 4]
    comb = combinations(a, 2)  # Todas las combinaciones con 2 numeros
    logger.info("list(comb): {}", list(comb))

    separator("COMBINATIONS WITH REPLACEMENT")  # Retorna todos los COMBINACIONES posibles entregandoles un length
    a = [1, 2, 3, 4]
    comb_wr = combinations_with_replacement(a, 2)
    logger.info("list(comb_wr): {}", list(comb_wr))

    separator("ACCUMULATE")  # Sumando en la iteracion, tambien se puede multiplicar
    a = [1, 2, 3, 4]
    acc = accumulate(a)
    logger.info("list(acc): {}", list(acc))

    separator_line()
    logger.info("ACCUMULATE multiplicacion")
    acc_mul = accumulate(a, func=operator.mul)
    logger.info("list(a): {}", list(a))
    logger.info("list(acc_mul): {}", list(acc_mul))

    separator("GROUPBY")  # Iterator que retorna key y values a partir de un obj iterator

    def smaller_than_3(x):
        return x < 3

    a = [1, 2, 3, 4]
    group_obj = groupby(a, key=smaller_than_3)
    for key, value in group_obj:
        logger.info("Key: {} - Value: {}", key, list(value))

    separator_line()

    logger.info("group_obj_lambda")
    group_obj_lambda = groupby(a, key=lambda x: x < 3)
    for key, value in group_obj_lambda:
        logger.info("Key: {} - Value: {}", key, list(value))

    separator_line()

    logger.info("group_obj_json")

    persons = [
        {'name': 'name1', 'edad': 18},
        {'name': 'name2', 'edad': 8},
        {'name': 'name3', 'edad': 2},
        {'name': 'name4', 'edad': 25},
        {'name': 'name5', 'edad': 25},
    ]
    group_obj_lambda = groupby(persons, key=lambda x: x['edad'])  # Agrupara por misma edad
    logger.info(" > 18")
    for key, value in group_obj_lambda:
        logger.info("Key: {} - Value: {}", key, list(value))

    separator_line()
    separator("COUNT")

    for i in count(10):  # Inicia desde 10 hasta infinito
        logger.info(i)
        if i == 15:
            break

    separator_line()
    separator("CYCLE")
    my_list = [1, 2, 3]
    for i in cycle(my_list):  # Empiezar a itrear de forma infinita en toda la secuencia del iterable
        logger.info(i)
        break

    separator_line()
    separator("REPEAT")
    for i in repeat(1):
        logger.info(i)  # Repite 1 infinatemente
        break

    for i in repeat(2, 10):
        logger.info(i)  # Repite 2 10 veces


def mainLambda():  # lambda arguments: expression
    separator("LAMBDA")
    separator_line()
    my_lamb = lambda x: x + 10
    logger.info("my_lamb: {}", my_lamb(5))
    separator_line()

    my_mult_lamb = lambda x, y: x * y
    logger.info("my_mult_lamb: {}", my_mult_lamb(5, 6))
    separator_line()

    points2d = [(1, 2), (15, 1), (5, -1), (10, 4)]
    points2d_sorted = sorted(points2d, key=lambda x: x[1])  # Sorted como 2o arg espera saber por donde ordenar
    logger.info("points2d: {}", points2d)
    logger.info("points2d_sorted: {}", points2d_sorted)

    separator_line()
    logger.info("MAP")  # map(func, seq)
    a = [1, 2, 3, 4, 5]
    b = map(lambda x: x * 2, a)
    logger.info("list(b): {}", list(b))

    separator_line()
    c = [x * 2 for x in a]  # Se obtiene el mismo resulta que arriba
    logger.info("c: {}", c)

    separator_line()
    logger.info("FILTER")  # filter(func, seq)
    a = [1, 2, 3, 4, 5, 6]
    b = filter(lambda x: x % 2 == 0, a)
    logger.info("b.filter: {}", list(b))

    separator_line()
    c = [x for x in a if x % 2 == 0]  # Filter 2
    logger.info("c: {}", list(c))

    separator_line()
    logger.info("REDUCE")  # filter(func, seq)
    a = [1, 2, 3, 4]
    product_a = reduce(lambda x, y: x * y, a)
    logger.info("product_a: {}", product_a)


class ValueToHighError(Exception):
    pass


class ValueToSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test_value(x):
    if x > 100:
        raise ValueToHighError('Value is to high')
    if x < 5:
        raise ValueToSmallError('Value is to high', x)


def mainExceptions():  # Errors and Exceptions
    try:
        test_value(3)
    except ValueToHighError as e:
        logger.error(e)
    except ValueToSmallError as e:
        logger.error(e.message)
        logger.error(e.value)


def mainLoggin():
    # logging.basicConfig(
    #     level=logging.DEBUG,
    #     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    #     datefmt='%m/%d/%Y %H:%M:%S')
    #
    # logging.debug("This is a debug message")
    # logging.info("This is a info message")
    # logging.warning("This is a warning message")
    # logging.error("This is a error message")
    # logging.critical("This is a critical message")

    separator_line()
    logger = logging.getLogger(__name__)

    # Create handler
    stream_h = logging.StreamHandler()
    file_h = logging.FileHandler('file.log')

    # Level and the format
    stream_h.setLevel(logging.WARNING)
    file_h.setLevel(logging.ERROR)

    # Formater
    formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')

    # Set formattter
    stream_h.setFormatter(formatter)
    file_h.setFormatter(formatter)

    # Add handlers
    logger.addHandler(stream_h)
    logger.addHandler(file_h)

    # loggers example
    logger.warning('This is a warning')
    logger.error('This is a error')

    separator_line()
    logger.warning("Config logger from file .conf")

    # Then use the config file in the code

    logging.config.fileConfig('logging.conf')

    # create logger with the name from the config file.
    # This logger now has StreamHandler with DEBUG Level and the specified format
    logger = logging.getLogger('simpleExample')

    logger.debug('debug message')
    logger.info('info message')
    import helper


def mainLogginError():
    # Loggear Execpcion especifica
    try:
        a = [1, 2, 3]
        val = a[4]
    except IndexError as e:
        logging.error(e, exc_info=True)

    # Loggear Execpcion especifica
    try:
        a = [1, 2, 3]
        val = a[4]
    except:
        logging.error("The error is %s", traceback.format_exc())


def mainLogginRotatingFile():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # Roll over after 2KB, and keep backup logs app.log.1 app.log.2 etc
    handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
    logger.addHandler(handler)

    for _ in range(10000):
        logger.info('hello world')


def mainLogginTimeRotatingFile():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # This will create a new log file every minute, and 5 backup files with a timestamp before overwriting old logs.
    handler = TimedRotatingFileHandler('timed_test.log', when='s', interval=5, backupCount=5)
    logger.addHandler(handler)

    for _ in range(6):
        logger.info('hello world')
        time.sleep(5)


def mainJson():
    # Object to JSON
    person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}
    personJSON = json.dumps(person, indent=2)
    personJSON_separator = json.dumps(person, indent=2, separators=(': ', '= '))
    personJSON_key = json.dumps(person, indent=2, sort_keys=True)  # Sort by abc
    logger.info("personJSON: " + personJSON)
    logger.info("personJSON_separator: " + personJSON_separator)
    logger.info("personJSON_key: " + personJSON_key)

    # Object to JSON.file
    with open('person.json', 'w') as file:
        json.dump(person, file, indent=2)

    person_dict = json.loads(personJSON)
    logger.info("person_dict: ")
    logger.info(person_dict)

    with open('person.json', 'r') as file:
        person_from_file = json.load(file)
        logger.info("person_from_file: ")
        logger.info(person_from_file)


class User:
    # Custom class with all instance variables given in the __init__()
    def __init__(self, name, age, active, balance, friends):
        self.name = name
        self.age = age
        self.active = active
        self.balance = balance
        self.friends = friends


def enconde_user(obj):
    if isinstance(obj, User):
        return {"name": obj.name, "age": obj.age, "type": obj.__class__.__name__}
    else:
        raise TypeError('Object of type User is not JSON serializablr')


def class_to_json():
    user = User('Max', 28, 1, 12, 'panas')
    userJson = json.dumps(user, default=enconde_user)
    logger.info("userJson: ")
    logger.info(userJson)


def MainRandom():
    random_random = random.random()
    logger.info("random_random")
    logger.info(random_random)

    random_uniform = random.uniform(1, 10)  # 10 NO esta incluido
    logger.info("random_uniform")
    logger.info(random_uniform)

    random_normalvariate = random.normalvariate(0, 1)  # Valores negativos y positivo
    logger.info("random_normalvariate")
    logger.info(random_normalvariate)

    mylist = list("ABCDEFG")
    random_choice = random.choice(mylist)
    logger.info("random_choice")
    logger.info(random_choice)

    random_sample = random.sample(mylist, 3)  # Devuelve 3 valores, NO repetidos
    logger.info("random_sample")
    logger.info(random_sample)

    random_choice = random.choices(mylist, k=3)  # Devuelve 3 valores, repetidos
    logger.info("random_choice")
    logger.info(random_choice)

    random.shuffle(mylist)
    logger.info("mylist.random_shuffle")
    logger.info(mylist)

    random_rand = np.random.rand(3)
    logger.info("random_rand")
    logger.info(random_rand)

    random_randint = np.random.randint(0, 10, (3, 4))  # Una tupla de 3 dimensiones
    logger.info("random_randint")
    logger.info(random_randint)


if __name__ == '__main__':
    MainRandom()
