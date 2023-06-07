file = open("test.txt")
# print(file.read())

#to readline
# it will read line by line
# print(file.readline())

line = file.readline()
while line!="":
    print(line)
    line = file.readline()

