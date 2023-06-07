ItemsInCart = 0

if ItemsInCart != 2:  #raise Exception("Products in cart are not matching")
    pass

assert (ItemsInCart == 0)

# Try and catch

try:
    with open("fileLog.txt",'r')as reader:
        reader.readline()

except Exception as e:
    print(e)
    # print("SOmehow i Have reached this block but couldent find FilelOg.txt")

finally:
    print("Cleaning up records , cache and cookies ")




