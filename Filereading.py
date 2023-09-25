file=open('abc.txt','r')

#for i in file:
#    print(i)
print(file.readlines())
file.seek(0)

# line = file.readline()
# while line != "":
#     print(line)
#     line=file.readline()

data= file.readlines()
for i in data:
    print(i)