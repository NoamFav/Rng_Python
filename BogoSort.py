import time
from itertools import pairwise
from random import randint
from random import shuffle


def is_sorted(data) -> bool:
    return all(a <= b for a, b in pairwise(data))


def bogosort(data):
    sorted_data = []
    while not is_sorted(data):
        shuffle(data)
        if min(data) == data[0]:
            sorted_data.append(data.pop(0))
            print("Sorted portion:", sorted_data, "Remaining data:", data)
    return data


if __name__ == '__main__':
    start = time.time()
    list_to_sort = [randint(0, 10000) for _ in range(1000)]
    sorted_list = bogosort(list_to_sort)
    end = time.time()

    print("Final list (attempt):", sorted_list)
    print("took {} seconds".format(end - start))
