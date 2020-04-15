# file = open("Demo.txt")
# # print(file.read())
#
# # print(file.read(4))
#
# # print(file.readline())
#
# # line = file.readline()
# # while line != "":
# #     print(line)
# #     line = file.readline()
#
# # for l in file.readlines():
# #     print(l)
#
# file.close()


with open("Demo.txt", 'r') as reader:
    content = reader.readlines()
    with open("Demo.txt", 'w') as writer:
        for line in reversed(content):
            writer.write(line)
