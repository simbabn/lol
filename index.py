def hello():
    print('hello world')

def name():
    name=str(input("enter the name : "))
    print('hello ' + str(name))

def sum():
    #instanciate the two numbers
    nbr1 = input('Entrez le premier nombre: ')
    nbr2 = input('Entrez le deuxième nombre: ') 
     
    s = int(nbr1) + int(nbr2)
    #printing
    print(s)

if __name__ == '__main__':
    hello()
    name()
    sum()