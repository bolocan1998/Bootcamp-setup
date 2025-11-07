name=input("Please enter your name: ")
age=int(input("How old are you {0} ?".format(name)))
print(f"Your age is {age}")

if age<18:
    print(f"You are not allowed to vote, because you are {age},and you have to wait")
elif age==900:
    print("Sorry man, you are a bit too late")
elif age>=18:
    print("You are welcomed")
#else:
    print("You are old enough to vote")
    print("Please put an X in the box")
# else:
#     print("You are not allowed to vote yet,please come back in {0}!!".format(18-age))