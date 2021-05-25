def fopen1(filename):
    file = open(filename, "w")
    file.write("Hello JAVA Programming...!")
    file.close()


def fopen2(filename):
    with open(filename, "w") as f:
        f.write("Hello Python Programming...!")


# fopen1("basic3.txt")
# fopen2("basic4.txt")


# read
def f_read(filename):
    with open(filename, "r") as f:
        contents = f.read()
    return contents


c = f_read("basic3.txt")
print(c)



