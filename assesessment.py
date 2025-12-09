# for i in range(1,11,2):
#   print(i)


# ### list comprehension!!!!!!!!
# num=[i for i in range(1,50)if i%3==0 ]
# print(num)

# st = 'Print every word in this sentence that has an even number of letters'
# for word in st.split():
#     if len(word) % 2 == 0:
#         print("even!",word)
st = 'Print only the words that start with s in this sentence'
# for word in st.split():
#     if word.startswith('s'):
#         print(word)

# num=[]
# for i in range(1,100):
#     if i % 3==0 and i % 5==0:
#         print("FizzBuzz")
#     elif i % 5 ==0:
#         print("Buzz")
#     elif i % 3==0:
#         print("Fizz")
#     else:
#         print(i)

st = 'Create a list of the first letters of every word in this string'
result=[word[0]for word in st.split()]
print(result)