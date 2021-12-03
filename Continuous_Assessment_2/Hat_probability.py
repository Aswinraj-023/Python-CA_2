# 4) b) Hat probability 
# Unique ID : E7321008

import random  # importing random function 
class limiterror(Exception): # crating user defined class for exception handling
  pass # No command needs to be given
class Hat(object):  # Creating a base class Hat
  def __init__(self,total_balls,balls_drawn): # defining constructor and attributes total no balls & drawn balls
    self.total_balls=total_balls  #assigning attribute values 
    self.balls_drawn=balls_drawn  # assigning attribute values
  def prob_calc(self):  # defining a method for probability calculation 
    self.drawn_lst=[]   # creating an empty list
    self.count_r=0 # assigning red ball count to 0
    self.count_b=0 # assigning blue ball count to 0
    self.count_g=0 # assigning green ball count to 0
    while self.total_balls < self.balls_drawn:  # until the total balls is less than no of ball drawn the below conditions will be executed
      try:  # using try & except
        if self.total_balls < self.balls_drawn:  # total balls is less than no of ball drawn
          raise limiterror  # limit error is raised
      except limiterror: #giving an exception for the error
        print(" total draw balls is greater than total no of balls") # handling the exception by printing a message
        self.balls_drawn=int(input("enter again:")) #Getting input from the user again
    else:  # if above conditions are false below conditions will run
      for i in range(self.balls_drawn):  # looping the below conditions till the range of value of balls drawn
        self.rand_num=random.randint(0,2)  #generating random numbers
        if self.rand_num == 0: #if randomn num is 0
          self.drawn_lst.append(self.r) # appending red ball to drawn list
            #print(self.drawn_lst)
          self.count_r+=1 # counting the occurance of red ball
        elif self.rand_num == 1:  #if randomn num is 1
          self.drawn_lst.append(self.b)  # appending blue ball to drawn list
          self.count_b+=1  # counting the occurance of blue ball
        elif self.rand_num == 2: #if randomn num is 2
          self.drawn_lst.append(self.g)  # appending green ball to drawn list
          self.count_g+=1 # counting the occurance of green ball
      print(self.drawn_lst) #printing the drawn list
      print("Probability of balls : \n","red =",self.count_r/self.total_balls,"Blue =",self.count_b/self.total_balls,"Green =",self.count_g/self.total_balls) # printing the probability of balls drawn
class Balls(Hat): #creating a class Balls and inheriting the attributes of base class
  def __init__(self,a,b): # defining constructor and attributes
    self.a=a   #assigning attribute values
    self.b=b   #assigning attribute values
  def red(self,total_balls,balls_drawn): #defining  method red
    Hat.__init__(self,total_balls,balls_drawn) #initializing the base class attributes
    self.r="red" #assigning attribute values
  def blue(self,total_balls,balls_drawn):  #defining  method red
    Hat.__init__(self,total_balls,balls_drawn)  #initializing the base class attributes
    self.b="Blue"   #assigning attribute values
  def green(self,total_balls,balls_drawn): #defining  method red
    Hat.__init__(self,total_balls,balls_drawn)  #initializing the base class attributes
    self.g="green"    #assigning attribute values
    Hat.prob_calc(self)  #calling the probability method from the base class
a=int(input("enter total no of balls:")) # getting the toal no: of balls as input
b=int(input("enter balls to be drawn:")) #getting the balls to be drawn as input
obj1=Balls(a,b) # invoking an object to derived class
obj1.red(a,b)  # finding the probability of red balls
obj1.blue(a,b)  # finding the probability of blue balls
obj1.green(a,b)  # finding the probability of green balls
