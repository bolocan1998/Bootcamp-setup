my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in my_list:
#     print(num)

for num in my_list:
    if num % 2 == 0:
        print(num,'is even')
    else:
        print(num, 'is odd')
print('* *'*30)
list_sum=0
for num in my_list:
    list_sum = list_sum + num
    print(list_sum)
print('* *'*30)

mystring='Hello my King'
for let in mystring:
    print(let)
print('* *'*30)

for _ in 'Welcome back dark knight':
    print(_, end=' ')
print('* *'*30)

myyyylist = [(1,2),(3,4),(5,6),(7,8)]    #### tuple unpaking####
for a,b in myyyylist:
    print(b,end=' ')
    print(a,end=' ')
print('* *'*30)
d={'k1':1,'k2':2,'k3':3}
for key,value in d:
    print(value)
