from loguru import logger
import sys

def my_generator():
    yield 3
    yield 1
    yield 2


def count_down(num):
    logger.info("Starting")
    while num > 0:
        yield num
        num -= 1


def firstn_normal(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums


def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1


def mainGenerators():
    g = my_generator()

    # for i in g:
    #     logger.info(i)

    # logger.info(next(g))
    # logger.info(next(g))
    # logger.info(next(g))

    # logger.info(sum(g))

    logger.info(sorted(g))

    cd = count_down(4)
    logger.info(next(cd))
    logger.info(next(cd))
    logger.info(next(cd))
    logger.info(next(cd))
    # logger.info(next(cd)) StopIteration Except

    logger.info(sys.getsizeof(firstn_normal(10000000)))
    logger.info(sys.getsizeof(firstn_generator(10000000)))


if __name__ == '__main__':
    mainGenerators()
