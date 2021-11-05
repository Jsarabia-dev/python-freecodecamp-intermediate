import time
from multiprocessing import Process
from threading import Thread, Lock
from loguru import logger
import os


def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)


def multiprocessing():
    processes = []
    num_processes = os.cpu_count()
    logger.info(num_processes)

    # Create processes
    for i in range(num_processes):
        p = Process(target=square_numbers)
        processes.append(p)

    # Start
    for p in processes:
        p.start()

    # Join
    for p in processes:
        p.join()

    logger.info("End main")


def threading():
    threads = []
    num_threads = 10

    # Create processes
    for i in range(num_threads):
        t = Thread(target=square_numbers)
        threads.append(t)

    # Start
    for t in threads:
        t.start()

    # Join
    for t in threads:
        t.join()

    logger.info("End main")


# all threads can access this global variable
database_value = 0


def increase_bad():
    global database_value  # needed to modify the global value

    # get a local copy (simulate data retrieving)
    local_copy = database_value

    # simulate some modifying operation
    local_copy += 1
    time.sleep(0.1)

    # write the calculated new value into the global variable
    database_value = local_copy


# LOCK
def increase_lock(lock):
    global database_value

    # lock the state
    lock.acquire()

    local_copy = database_value
    local_copy += 1
    time.sleep(0.1)
    database_value = local_copy

    # unlock the state
    lock.release()


def threading_lock():
    # create a lock
    lock = Lock()

    print('Start value: ', database_value)

    # pass the lock to the target function
    t1 = Thread(target=increase_lock, args=(lock,))  # notice the comma after lock since args must be a tuple
    t2 = Thread(target=increase_lock, args=(lock,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('End value:', database_value)

    print('end main')


# WITH LOCK - Recommended form
def increase_with_lock(lock):
    global database_value

    with lock:
        local_copy = database_value
        local_copy += 1
        time.sleep(0.1)
        database_value = local_copy


if __name__ == "__main__":
    # multiprocessing()
    # threading()
    threading_lock()
