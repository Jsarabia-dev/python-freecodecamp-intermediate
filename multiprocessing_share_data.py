import os
import time
from multiprocessing import Process, Value, Array, Lock, Queue, Pool
from multiprocessing import Queue

from loguru import logger


def add_100(shared_number):
    for i in range(100):
        time.sleep(0.01)
        shared_number.value += 1


def main_processing_with_race_conditions():
    print("===== main_processing_with_race_conditions ==== ")

    shared_number = Value('i', 0)  # i: Integer value
    print("shared_number:", shared_number.value)

    p1 = Process(target=add_100, args=(shared_number,))
    p2 = Process(target=add_100, args=(shared_number,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("shared_number final:", shared_number.value)


def add_100_lock(shared_number, lock):
    for i in range(100):
        time.sleep(0.01)
        # lock.acquire()
        with lock:
            shared_number.value += 1
        # lock.release()


def main_processing_with_lock():
    print("===== main_processing_with_lock ==== ")
    shared_number = Value('i', 0)  # i: Integer value
    lock = Lock()

    print("shared_number:", shared_number.value)

    p1 = Process(target=add_100_lock, args=(shared_number, lock))
    p2 = Process(target=add_100_lock, args=(shared_number, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("shared_number final:", shared_number.value)


def add_100_array(shared_numbers, lock):
    for i in range(100):
        time.sleep(0.01)
        for r in range(len(shared_numbers)):
            with lock:
                shared_numbers[r] += 1


def main_processing_array():
    print("===== main_processing_array ==== ")
    shared_array = Array('d', [0.0, 100.0, 200.0])  # d: Double value
    lock = Lock()

    print("shared_array:", shared_array[:])

    p1 = Process(target=add_100_array, args=(shared_array, lock))
    p2 = Process(target=add_100_array, args=(shared_array, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("shared_array final:", shared_array[:])


def square(numbers, queue):
    for i in numbers:
        queue.put(i * i)


def make_negative(numbers, queue):
    for i in numbers:
        queue.put(i * -1)


def main_processing_queue():
    print("===== main_processing_queue ==== ")
    numbers = range(1, 6)
    q = Queue()

    p1 = Process(target=square, args=(numbers, q))
    p2 = Process(target=make_negative, args=(numbers, q))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    # order might not be sequential
    while not q.empty():
        print(q.get())

    print('end main')


def cube(number):
    return number * number * number


def main_processing_pool():
    print("===== main_processing_pool ==== ")

    numbers = range(10)

    p = Pool()

    # by default this allocates the maximum number of available
    # processors for this task --> os.cpu_count()
    result = p.map(cube, numbers)

    # or
    # result = [p.apply(cube, args=(i,)) for i in numbers]

    p.close()
    p.join()

    print(result)


if __name__ == "__main__":
    # main_processing_with_race_conditions()
    # main_processing_with_lock()
    # main_processing_array()
    main_processing_queue()
