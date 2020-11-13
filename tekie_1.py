# Write a python program that finds the second largest number from a given list of numbers

import random

#Generating a random list
test_list = random.sample(range(0,100), 5)
print("The randomly generated list is:", test_list)

def second_larget(lst):
    x = max(lst)
    lst.remove(x)
    return max(lst)

answer = second_larget(test_list)
print("The second largest number is:", answer)