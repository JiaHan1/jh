import random


if __name__ == '__main__':
    array = ['a', 'b', 'c']
    for i in range(100):
        print(array[random.randint(0, len(array)) - 1])
