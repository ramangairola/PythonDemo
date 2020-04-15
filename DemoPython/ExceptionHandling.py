# i=0
#
# # if i!=1:
# #     raise Exception("Exception")
#
# assert (i==1)

try:
    with open("emo.txt" ,'r') as reader:
        reader.read()

except Exception as e:
    print(e)