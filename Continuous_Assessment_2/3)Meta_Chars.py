# 3) Meta characters

import re #importing library "regular expression"
def is_allowed_specific_char(input_str): #defining a method 'is_allowed_specific_char' with an attribute 'input_str'
    pattern="^[|a-z|A-z]....[f|F]" #Using 'meta characters' to match the characters from A to f in the input string
    result=re.match(pattern,input_str) # Using the library function for matching the pattern in the input string 
    print(result)  #Printing the result
input_str=str(input("Enter the characters : ")) #Getting input string from the user
is_allowed_specific_char(input_str) #calling the function 

#if the pattern doesnt match the given string, the output will be "NONE"



