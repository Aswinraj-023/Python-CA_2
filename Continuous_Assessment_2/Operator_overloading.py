# 2)Operator Overloading  (Unique ID : E7321008)
 
class Operator(): #creating a class named Operator
  def __init__(self,a): #initializing constructor and defining attributes
    self.a=a  #assigning value to attribute 
  def __sub__(self,b): #creating a magic function and defining attribute
    return self.a-b.a  #defining the calculation part in return statement
  def __neg__(self,c): #creating a magic function and defining attribute
    return -self.c    #defining the calculation part in return statement
print("Choose the Options : ", "\n 1. Difference between two complex numbers","\n2. Negative of a number") #Asking the user to choose an option
option = int(input("Option : "))  #Getting input from the user
while option>0:  # Until option is greater than zero the following conditions will be executed
    if option==1: #if the value of 'Option" is 1 the magic method __sub__ will be executed
        obj1=Operator(complex(input("Enter the complex number 1 : "))) #Getting input from the user as complex number 
        obj2=Operator(complex(input("Enter the complex number 2 : ")))  #Getting input from the user as complex number
        print("Difference between given complex numbers are : ",obj1-obj2)  # Printing the difference between given complex numbers
        print("______________________________________________________________") 
        option=int(input("Enter 0 to exit or continue the process \n Option : ")) #Asking the user to input an option
    elif option==2:   #else if option is equal to 2 the magic method __neg__ will be executed
        obj3=int(input("Enter the number : "))  # Getting input from user
        N=obj3.__neg__() # calling the magic method __neg__
        print("Negative of ",obj3,"is : ",N)  #Printing the negative of the given number
        print("_______________________________________________________________")
        option=int(input("Enter 0 to exit or continue the process \n Option : "))   #Asking the user to input an option
    elif option>2:  #else if option is greater than 2 the following will be executed
        option=int(input("Invalid choice ! Please enter again \n option : "))  #Asking the user to input an option
    else:
        option=int(input("Enter 0 to exit or continue the process \n Option : ")) #Asking the user to input an option
        
