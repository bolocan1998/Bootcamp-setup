celcius=[10,20,30,43.5]
fahrenheit = [((9/5)*temp + 32)for temp in celcius]
#print(celcius)
#print(fahrenheit)
fahrenheit =[]
for tem in celcius:
    fahrenheit.append(((9/5)*tem+32))
print(fahrenheit)

