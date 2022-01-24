# Students = [['Harry', 37.21], ['Berry', 32], ['Cherry', 37.21], ['Jerry', 45], ['Marry', 22]]
# code to output second lowest score from the above list, if second lowest score is repeated then print the names
# of students in alphabetical order

d = {}
N = int(input("Enter the range of name value pair: "))
print(N)
for i in range(0, N):
    names = input("Enter name: ")
    score = float(input("Enter score: "))
    d[names] = score

score_list = sorted(set(d.values()))[1]
print(score_list)

names_list = []

for key,value in d.items():
    if value == score_list:
        names_list.append(key)

for name in sorted(names_list):
    print(name)