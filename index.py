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

def sum_n():
    n=(int)(input("enter the number : "))
    result= n*(n+1)
    result = int(result/2)
    print(result)

def palindrome():
    #Getting the string
    my_str = input('Entrez le premier mot: ') 
    my_str = my_str.casefold()
    #reverse the string
    rev_str = reversed(my_str)

    #test if strings are the same
    if list(my_str) == list(rev_str):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")



if __name__ == '__main__':
    # hello()
    # name()
    # sum()
    # sum_n()
    palindrome()