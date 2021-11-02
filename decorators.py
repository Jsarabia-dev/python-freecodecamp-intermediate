from loguru import logger
import functools


def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Do ...
        logger.info("Start")

        result = func(*args, **kwargs)

        # Do ...
        logger.info("End")
        return result

    return wrapper


@start_end_decorator  # Option 2
def print_name():
    logger.info("Alex")


# print_name = start_end_decorator(print_name) Option 1

@start_end_decorator
def add5(x):
    logger.info(x + 5)


if __name__ == '__main__':
    print_name()
    add5(1)
