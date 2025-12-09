x=50
def func(x):
    print(f'X is {x}')
#LOCAL REASSIGNEMENT ON A GLOBAL VAIRABLE!
    x='NEW VALUE'
    print(f'I JUST LOCALLY CHANGED GLOBAL X TO {x}')
    return x
print(x)