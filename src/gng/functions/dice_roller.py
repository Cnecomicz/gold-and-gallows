import random


def roll_x_d_n_and_keep_highest_k(x, n, k):
    result = 0
    results_list = []
    for i in range(x):
        results_list.append(random.randint(1, n))
    for j in range(k):
        highest = max(results_list)
        result += highest
        results_list.remove(highest)
    return result


def roll_x_d_n(x, n):
    return roll_x_d_n_and_keep_highest_k(x, n, x)


def thread_the_needle(low, high):
    """Returns a bool based on if a d20 die roll is strictly between the 
    two given inputs."""
    return low < roll_x_d_n(1, 20) < high


def roll_below(value):
    """Returns a bool based on if a d20 die roll is strictly below the given
    input."""
    return thread_the_needle(0, value)


def roll_above(value):
    """Returns a bool based on if a d20 die roll is strictly above the given
    input."""
    return thread_the_needle(value, 21)
