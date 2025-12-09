# def square(num):
#     return num**2
# my_num=[1,2,3,4]
# for itme in map(square,my_num):
#   #  print(itme)
#     print(list(map(square,my_num)))

def splicer(mystring):
    if len(mystring)%2==0:
        return 'EVEN'
    else:
        return mystring[0]
names=['Andy','Garcia','Peter','Ana']
print(list(map(splicer,names)))