# Task
# Given  sets of integers,  and , print their symmetric difference in ascending order. The term symmetric difference indicates
# those values that exist in either  or  but do not exist in both.
#
# Input Format
#
# The first line of input contains an integer, .
# The second line contains  space-separated integers.
# The third line contains an integer, .
# The fourth line contains  space-separated integers.
#
# Output Format
#
# Output the symmetric difference integers in ascending order, one per line.

# Sample Input
#
# STDIN       Function
# -----       --------
# 4           set a size M = 4
# 2 4 5 9     a = {2, 4, 5, 9}
# 4           set b size N = 4
# 2 4 11 12   b = {2, 4, 11, 12}

# Sample Output
#
# 5
# 9
# 11
# 12

M = int(input())
a = set()
a_string = input()
for x in a_string.split():
    a.add(int(x))
N = int(input())
b = set()
b_string = input()
for x in b_string.split():
    b.add(int(x))

a_sorted = a.difference(b)
b_sorted = b.difference(a)
set_union = a_sorted.union(b_sorted)
for x in sorted(set_union):
    print(x)