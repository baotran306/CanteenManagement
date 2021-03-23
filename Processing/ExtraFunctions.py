import numpy as np


def random_index(num_of_food):
    arr = np.random.permutation(20)
    return arr[:num_of_food]


# if __name__ == "__main__":
#     print(random_index(15))
