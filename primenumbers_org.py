# Write Python code to find if ALL the numbers in a given list of integers are PART of the series defined by the following.
# f(0) = 0 f(1) = 1 f(n) = 5*f(n-1) - 2*f(n-2) 
# for all n > 1. def is_part_of_series(lst):
import random
import sys

sys.setrecursionlimit(2500)

series_list = [0,1]
test_list = []


def series():
    ele = len(series_list)
    return ((5*series_list[ele-1])-(2*series_list[ele-2]))


def is_part_of_series(lst):
    result_list = []
    for x in lst:
        if x > 0:
            if x in series_list:
                result_list.append(x)
            else:
                while True:
                    if series_list[-1] > x:
                        break
                    new_term = series()
                    series_list.append(new_term)
                    if x in series_list:
                        result_list.append(x)
                        break
                    elif new_term > x:
                        break
        # print(lst.index(x))
    return result_list

test_list = random.sample(range(1, 1000000), 10000)
test_list.extend(random.sample(series_list, 10))
result = is_part_of_series(test_list)

print("***********", result)