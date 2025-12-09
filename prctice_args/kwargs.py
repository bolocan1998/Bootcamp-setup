# def myfunc(*args):
#     return[num for num in args if num%2==0]
# print(myfunc(1,2,3,4,5))

def myfunc(x):

    out = []

    for i in range(len(x)):

       if i%2==0:
           out.append(x[i].lower())

       else:

           out.append(x[i].upper())
    return ''.join(out)