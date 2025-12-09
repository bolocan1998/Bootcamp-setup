###                            Plus the functions [break, continue, pass]
# x=0
# while x<5:
#     print(f"The value of x is {x}")
#     x=x+1
# else:
#     print("X is not less than 5")
# print("* *"*20)

# x=[1,2,3]
# for item in x:
#     pass       ### this function does nothing
# print("The end of my script")

# mystring='Sammy'
# for letter in mystring:
#     if letter=='a':
#         continue
#     print(letter)
mystring='Sammy'
for letter in mystring:
    if letter=='m':
        break
    print(letter)


