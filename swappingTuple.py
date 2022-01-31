# You are given two integers. Store them in 2 variables, send those variables to a function which will return a tuple with
# swapped values. Print that tuple. Easy enough!
# Only one line is allowed in the function body.

import re
num1 = input()
num2 = input()
list1 = list()


def swap_integers(n1, n2):
    regex = re.compile(r'[\r\n\t]')
    n1 = regex.sub("", n1)
    n1, n2 = n2, n1
    list1.append(int(n1))
    list1.append(int(n2))
    new_tuple = tuple(list1)
    return new_tuple


tuple_variable = swap_integers(num1, num2)
print(tuple_variable)