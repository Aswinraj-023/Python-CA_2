#1 Subject_list & Class_list

class Subject_list(): # creating a class Subject_list
  def __init__(self): #defining a constructor and attributes
    self.name=[]  #Creating variable list
    self.marks=[] #creating variable list
    self.test_grades=[]  #creating test grades list
  def get_input(self):  #defining method 'get_input'
    self.n=int(input("Enter the number of Students to be graded : "))   #getting input from user
    for i in range(self.n):   #looping the input of marks & names till the range of 'n'
      self.student_report=[]  #creating student report list
      self.name=list(map(str,input("Enter First Name & Last Name : ").split()))  #getting name as input as list
      self.marks=input("Enter the Marks : ")  #getting marks as input 
      self.marks=list(map(float,self.marks.split()))  # mapping the marks into float inside list
      self.student_report.append(self.name) #adding name into student_report list
      self.student_report.append(self.marks)  #adding marks into student_report list
      self.test_grades.append(self.student_report)  #adding student_report list into test_grades list
    print("Test grades =",self.test_grades) # printing Test grades
class Class_list(Subject_list): #creating a class named Class_list
  def __init__(self):   # defining a constructor and attributes
    self.class_lst=[] # creating an empty class list
    Subject_list.__init__(self)  #initializing the initialization attributes of  class Subject_list
  def average(self):  # defining a method average
    Subject_list.get_input(self) #calling the attributes of  class Subject_list
    for i in range(self.n): # Looping the no: of students to be graded for calculating the average
      try:  # Using try & except error handling
        self.avg=sum(self.test_grades[i][1])/len(self.test_grades[i][1])  # Calculating the average of marks
        #self.test_grades[i].append(self.avg)
      except ZeroDivisionError:   # Replacing the Zero Division error with a print statement
        print("NO GRADE FOR A STUDENT")
        self.test_grades[i].append([])  # adding an empty list to test_grades 
      else:  # if the above condition is false
        self.test_grades[i].append(self.avg)  # adding the average to the test_grades list
        #self.class_lst.append(self.test_grades)
      #print(self.test_grades)
    for i in range(self.n): # looping the no: of students to be graded fo deleting the average if marks list is empty
      if [] in self.test_grades[i]:  #if the marks list in test grades list is empty
        self.test_grades[i].append([]) #adding an empty list 
        del self.test_grades[i][2]  # deleting the average of other marks
        
      else:  # if above condition is false
        self.class_lst  #returning test_grades
    self.class_lst.append(self.test_grades)  #adding test_grades list to class list
    print("Class List = ",self.class_lst)  #printing the class list
obj=Class_list()  # invoking the object to Class_list
obj.average() # calling the average method using the object
