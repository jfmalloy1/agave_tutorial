""" Code adopted from https://www.machinelearningplus.com/python/parallel-processing-python/
"""
import numpy as np
from time import time


### Prepare data
def get_data():
    """ Makes a 2D array, with 200000 subarrays of size 5, all with random integers between 0 and 9

    Returns:
        [list]: see above
    """
    np.random.RandomState(100)
    #Size makes a list of 200k sublists, each of length 5
    arr = np.random.randint(0, 10, size=[200000, 5])
    data = arr.tolist()
    #Prints the first 5 sublists
    print("Data:", data[:5])
    return data


def howmany_within_range(sublist, minimum, maximum):
    """Returns how many numbers lie within `maximum` and `minimum` in a given `row`"""
    count = 0
    for n in sublist:
        if minimum <= n <= maximum:
            count = count + 1
    return count


def main():
    data = get_data()
    results = []
    start = time()

    #Finds how many random numbers are between min and max in each sublist
    for row in data:
        results.append(howmany_within_range(row, minimum=4, maximum=8))

    print("Time elapsed:", time() - start)

    print("Numbers in range 4-8:", results[:5])


if __name__ == "__main__":
    main()
