#Asa verificam versiunea de python care ruleaza!!
# from platform import python_version
# print(python_version())

# def say_hello(jelly):
#     print(f"Hello {jelly}")
# say_hello("John")

# def return_result(a,b,c):
#     return a+b+c
# result = return_result(5,5,5)
# print(result)

# def even_chech(number):
#     return number%2==0
# print(even_chech(22))

def chech_even_list(num_list):          #REturn all the even numbrs in a list

    even_numbers=[]
    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass
    return even_numbers
print(chech_even_list([1,3,5]))