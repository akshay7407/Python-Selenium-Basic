file = open("test.txt")

# optional way to open file and close
# with open("test.txt") as file:
#
# To read full file
# print(file.read())

#Using  readline
# it will read line by line

# line = file.readline()
# while line!="":
#     print(line)
#     line = file.readline()


#     USing readlines method

txtLine = file.readlines()
for lin in txtLine:
    print(lin)
file.close()
