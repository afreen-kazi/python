# A valid mobile number is a ten digit number starting with a 7, 8 or 9.

import re
N = int(input())

for i in range(0, N):
    string = input()
    reg_exp = r"^[789]\d{9}$"
    if re.match(reg_exp, string):
        print("YES")
    else:
        print("NO")

# first occurrence of 7,8 or 9, followed by repeating \d => [0-9] 9 times (9 digit)