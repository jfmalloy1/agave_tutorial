""" Code adopted from https://www.machinelearningplus.com/python/parallel-processing-python/
"""
import numpy as np
from time import time
import multiprocessing as mp


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

    # Step 1: Init multiprocessing.Pool()
    print("CPU count:", mp.cpu_count())
    pool = mp.Pool(mp.cpu_count())

    #Finds how many random numbers are between min and max in each sublist
    # Step 2: `pool.apply` the `howmany_within_range()`
    start = time()
    results = [
        pool.apply(howmany_within_range, args=(row, 4, 8)) for row in data
    ]
    print("Time elapsed (apply):", time() - start)

    start = time()
    results = pool.starmap(howmany_within_range, [(row, 4, 8) for row in data])
    print("Time elapsed (starmap):", time() - start)

    # Step 3: Don't forget to close!
    pool.close()

    print("Numbers in range 4-8:", results[:5])


if __name__ == "__main__":
    main()
