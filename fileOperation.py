# In this question, the user will enter a file name and you are required to read that file and print the number of
# words in it. Simple ain't it!

filename = "word.txt"

file1 = open(filename, 'w')
file1.write("It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).")
file1.close()

line = []
file2 = open(filename, 'r')
content = file2.read()
string = ''
for line in content:
    string += line
separator = string.split()
print(len(separator))