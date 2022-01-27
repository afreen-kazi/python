# input
# 3
# 07895462130
# 919875641230
# 9195969878

# output
# +91 78954 62130
# +91 91959 69878
# +91 98756 41230

# first line will contain no. of mobile numbers, get mobile number and then put prefix +91 before each mobile number
listing = ['07895462130', '919875641230', '9195969878']
list1 = []
list2 = []
# str1 = "+91 "


def add_separator(string):
    prefix = "+91"
    new_string1 = ''
    new_string2 = ''
    new_one = ''
    str1 = slice(0, len(string) // 2)
    str2 = slice(len(string) // 2, len(string))
    for i in string[str1]:
        new_string1 += i
    for i in string[str2]:
        new_string2 += i
    new_one = prefix + " " + new_string1 + " " + new_string2
    return new_one


new_list = []
for x in listing:
    if len(x) == 11:
        string = x[1:]
    elif len(x) == 12:
        string = x[2:]
    else:
        string = x
    list2.append(string)

new_list = sorted(list2)
print(new_list)

total = ''
for x in sorted(new_list):
    total += add_separator(x)

print(total)
