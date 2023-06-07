with open("test.txt",'r') as reader:
    content = reader.readlines()
    print(content)
    with open('test.txt','w') as writer:
        writer.write("I love my job \n I am software tester ")

