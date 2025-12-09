#Global
name='This is a global string'

def greet():
  #Enclosing
    name='Sammy'

    def hello():
        #Local
        name='I AM LOCAL'
        print('Hello '+ name)

    hello()
greet()

