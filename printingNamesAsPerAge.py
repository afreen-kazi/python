# You are given some information about  people. Each person has a first name, last name, age and sex. Print their names
# in a specific format sorted by their age in ascending order i.e. the youngest person's name should be printed first.
# For two people of the same age, print them in the order of their input.

# nested_list = [['Mike', 'Thomson', '20', 'M'], ['Robert', 'Bustle', '32', 'M'], ['Andria', 'Bustle', '30', 'F']]
#
#
# def sort(n_list):
#     n_list.sort(key = lambda x: x[2])
#     return n_list
#
#
# print(sort(nested_list))
# for x in nested_list:
#     if x[3] == 'M':
#         abb = 'Mr.'
#     elif x[3] == 'F':
#         abb = 'Ms.'
#     print(abb, x[0], x[1])


#############################################333333
# solved in hackerrank

def person_lister(f):
    def sort_function(people):
        people.sort(key=lambda x: x[2])
        return people

    list = []

    def abb(value):
        return "Mr. " if value == "M" else "Ms. "

    def inner(people):
        li = sort_function(people)
        for x in li:
            list.append(abb(x[3]) + x[0] + " " + x[1])
        return list
        # complete the function

    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print('\n'.join(name_format(people)))
