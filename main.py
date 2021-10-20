import sys
from timeit import default_timer as timer
from loguru import logger

from collections import Counter, namedtuple, OrderedDict, defaultdict, deque
from itertools import *
import operator

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

    separator("GROUPBY")  # Iterator que retorna key values


if __name__ == '__main__':
    mainItertools()