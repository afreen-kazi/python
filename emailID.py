import re
email_id = "afreen7kazi@forgeahead.co"


# def fun(string):
#     flag = False
#     string1 = string.split('.')
#     # print(string1)
#     ext = string1[1]
#     # ext_verify = bool(re.match(r"^[a-zA-Z]+$", ext))
#     ext_verify = bool(re.match(r"^(\w{2,3})+$", ext))
#     # print(ext_verify)
#     username = string1[0]
#     new_string = username.split('@')
#     user = bool(re.match(r"^[a-zA-Z\d_]+[.-]*$", new_string[0]))
#     # print(user)
#     website = bool(re.match(r"[a-zA-Z\d]+$", new_string[1]))
#     # print(website)
#     if ext_verify == True and len(ext) == 3 and user == True and website == True:
#         flag = True
#     return flag


def fun(string):
    # flag = False
    print(string)
    reg_exp = r"^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{3})+$"
    flag = bool(re.match(reg_exp, string))
    return flag


print(fun(email_id))

# [a-zA-Z0-9_]+ is same as \w+
# email id regular expression =
# ^\w+([.-]?\w+)*@\w+([.-]?\w)*(\.\w{2,3})+$
# \w = [a-zA-Z0-9_]+ (1 or more occurrence of letter, number or underscore)
# + means one or more occurrence
# * means zero or more occurrence
# [.-]? means matches an optional character . or -
# @ matches itself
# \. matches the .com's (.) character
# and \w{2,3} will match com/org/io/.. extensions



