# my_dictionary={'key1':'value1','key2':'value2','key3':'value3'}
# #print(my_dictionary['key1'])
# for key in my_dictionary:
#     print(my_dictionary[key],end="   ")

# price_lookup={'apple':1.99,'kiwi':1.45,'banana':1.24,'oranges':2.33}
# print(price_lookup['apple'])
#
# for key in price_lookup:
#     print(key,price_lookup[key],end="     ")

# d={'k1':123,'k2':[1,2,3],'k3':{'insideKey':130},'k4':['a','b','c']}
# print( d['k3']['insideKey'])
# print(d['k2'][1])
# print(d['k1'])
# print(d['k4'][2].upper())

d={'k1':100,'k2':200}
d.update({'k2':'alter'})
d.update({'k3':350})
print(d.keys(),end=' ')
print()
print(d.values(),end=' ')
print()
print(d.items(),end=' ')    #####tuples######

