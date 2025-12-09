# def myfunc(a,b):          #deoarece aici am specificat doar 2,
#     return sum((a,b))*0.05
# print(myfunc(30,40))  #aici avem numar limitat de argumente pe care le putem introduce(daca intrducem mai multe
# ##primim o eroare!!!!!!!!!

# def myfunc(*args):          #iar in loc de *args putem folosi care termen vrem
#     for item in args:
#         print(item)
#     return sum(args)*0.05
#
# print(myfunc(30,30,50,100,500,1000))

# def myfun(**kwargs):
#     print(kwargs)
#     if 'fruit'in kwargs:
#         print(f'My fruit of choice is {kwargs["fruit"]}')
#     else:
#         print('I did not find any fruit here')
# print(myfun(**{'fruit':'apple','veggie':'lettuce'}))

def myfunc(*args, **kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0], kwargs['food']))
print(myfunc(10,20,30,fruit='apple',food='eggs',animal='dog'))
