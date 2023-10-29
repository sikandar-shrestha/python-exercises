#!/usr/bin/env python
# coding: utf-8

# Q1)Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.


def is_two(x):
    "function accepts either no 2 or string 2"
    if x==2 or x=='2':
        
        return True
    else:
        
        return False






## Another way
def is_two(num):
    if num in (2,'2',2.0):
        return True
    else: 
        return False







# Q2)Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.




## 1st way
def is_vowel(x):
    if x in ['a','e','i','o','u']:
        return True
    else:
        return False




## 2nd way
def is_vowel(x):
    vowels='AEIOUaeiou'
    return x in vowels





# 3rd way:
def is_vowel(somestring):
    #check that the arg is a str
    if type(somestring) == str:
        
        # if the str is 1 char and a letter
        '''
        isalpha() method returns True if all the characters 
        are alphabet letters(a-z)
        
        '''
        if len(somestring) == 1 and somestring.isalpha():
            
            #return bool ans to: lower-letter in vowel list?
            return somestring.lower() in list('aeiou')
        
        #return false if string fails 1 alpha-char length
        else:
            return False
        
    # returns false if input is not a str    
    else:
        return False
        




# Q3)Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.




def is_consonant(x):
    
    return not is_vowel(x)




## 2nd way
def is_consonant(somestring):
    """
    This function will:
    - intially check the input is a string
        - and 1 char long
        - and a letter
            -if true, returns the opposite return of is_vowel, using the NOT operator
            - False otherwise
    -returns False if not a string
    """
    if type(somestring) == str:
        if len(somestring) == 1 and somestring.isalpha():
            return (not is_vowel(somestring))
        else:
            return False
    else: 
        return False
            





# Q4) Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.



def capital_word(word):
    if is_consonant(word[0]):
        return word.capitalize()
    return word





# Another way
def capitalize_starting_consonant(word):
    """
    This function will initially check if:
    - input is a str
        - checks if 1st char of the input is a consonant
            - if True, returns the inputted string w/1st char Capitalized
            - False otherwise
        - returns False if not a string
    """
    if type(word) == str:
        if is_consonant(word[0]):
            return word.capitalize()
        else:
            return f"{word} doesn't start with a consonant."
    else:
        return f"{word} isn't a string."


# Q5)Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.




def calculate_tip(tip_percent,bill): # tip_percent & bill are parameters
    if 0<=tip_percent<=1:
        tip_amount=tip_percent*bill
        return tip_amount
    else:
        return "Invalid tip %"
    




# Q6) Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.




def apply_discount(price,discount_percent):
    if 0<=discount_percent<1:
        discount=discount_percent*price
        price=price-discount
        return price
    else:
        return 'Invalid discount %'
    




## Another way

def apply_discount(orig_price, discount_pct):
    return (1 - discount_pct)* orig_price


# Q7) Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.



def handle_commas(string):
    return float(string.replace(",",""))




    




## Another way

#def handle_commas(fakenum):
    """
    This function will:
    - check if input is a string
        -removes any commas
        -check if the stripped input is a digit
            - if True, returns input as an integer
            -False otherwise
    - if not a string, returns false stmt
    """
    #if type(fakenum) == str:
     #   stripfakenum = fakenum.replace(",", "")
    #    if stripfakenum.isdigit():
   #         return int(stripfakenum)
    #    else:
   #         return False
  #  else:
 #       return False
    



# Q8) Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).




def get_letter_grade(num):
    if num>=90:
        return "A"
    elif num>=80:
        return "B"
    elif num>=70:
        return "C"
    elif num>=60:
        return "D"
    else:
        return "F"





## Another way
def get_letter_grade(somegrade):
    if type(somegrade) == int:
        if somegrade >= 90:
            return 'A'
        elif somegrade >= 80:
            return 'B'
        elif somegrade >= 70:
            return 'C'
        elif somegrade >= 60:
            return 'D'
        else: return 'F'
    else:
        return f"{somegrade} is not a digit."
        


# Q9) Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.




def remove_vowels(string):
    new_string=" "
    
    for x in string:
        if x not in "AEIOUaeiou":
            new_string +=x
        
        else:
            pass
    return new_string
            







## Another way
# adding to remove
def remove_vowels(word):
    # empty string for items to keep
    new_word = ""
    
    # loop iteration over word 
    for letter in word:
        
        # conditional check for whether letter in word is not a vowel. 
        
        if not is_vowel(letter):
        # if not in list('aeiou'): # alternative way
            
            # If so, add to empty string
            new_word += letter
            
    # return concatenated empty string
    return new_word


# Q10) Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# 
# - anything that is not a valid python identifier should be removed
# - leading and trailing whitespace should be removed
# - everything should be lowercase
# - spaces should be replaced with underscores
# - for example:
#         
#         - Name will become name
#         
#         - First Name will become first_name
#         
#         - % Completed will become completed

# In[ ]:


def normalize_name(string):
    string = string.strip()
    for x in string:
        if not x.isalnum():
            if x != " ":
                string = string.replace(x,'')
                string = string.strip()
                
            else:
                string = string.replace(x,"_")
        else:
            pass
    return string.lower()



    





## 2nd way
def normalize_name(string):
    string=string.lower()
    string=string.strip()
    string=string.replace(" ","_")
    for x in string:
        if not x.isalnum():
            if x!="":
                string=string.replace(x,'')
                string=string.strip()
            else:
                string = string.replace(x,"_")
        else:
            pass
    return string





## 3rd way
'''
Valid Python Identifiers
An identifier can only contain letters, digits, and underscores, and cannot start with a digit

- empty string to to append to 
- check if first letter starts with a digit
    - for letter in string:
        - check if string is a letter, digit, or underscore
            - remove leading & trailing whitespace
            - replace space in string with underscore
            
returns normlaized string

'''

def normalize_name(somestr):
    # empty string to concatenate to
    new_string = ''
    
    # strip whitespace first else problems and lower case string as asked
    somestr = somestr.strip().lower()
    
    

    # loop over passed string and add letters and spaces but not numbers
    for char in somestr:
        if char.isalpha() or char == ' ':

                 new_string+= char # now need to strip any white space characters again in return if num remove
    
    
    return new_string.strip().replace(' ', '_') 


# Q11) Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# 
#         -cumulative_sum([1, 1, 1]) returns [1, 2, 3]
#         -cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]
# 




def cumulative_sum(num):
    for x in range(len(num)):
        if x !=0:
            num[x]=num[x]+num[x-1]
    return num










def cumulative_sum(oldlist):
    
    newlist=[]
    
    #intialize a variable to store the cumulative sum
    c_sum = 0
    
    for num in oldlist:
        #add the current number to the cumulative sum
        c_sum += num
        #print(f"cumulative: {c_sum}")
        #append the cumulative sum to the newlist
        newlist.append(c_sum)
    print(f'oldlist: {oldlist}')
    print(f"newlist: {newlist}")







#remark for understanding function with loop
'''
def is_alplha(string):
    new_string=''
    for letter in string:
        if letter.isalpha(): # to check for letters
            new_strin +=letter
        else:
            pass
    return new_string
'''


# BQ1) Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. Bonus write a function that does the opposite.




def twelveto24(time):
    
    # separate hours and minutes
    time = time.split(':') # split at colon as list
    hour = time[0] # store hrs in variables
    mins = time[1].split(' ') # store minutes in list
    minutes = mins[0] # store min in var
    timeofday = mins[1] # store time of day in var
    
    if timeofday.lower() == 'pm':
        
        hour = 12 + int(hour)

        return str(hour) + ':' + str(minutes) + timeofday
    else:
      
        return hour + ':' + minutes + timeofday






# BQ2) Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
# 
# -col_index('A') returns 1
# 
# -col_index('B') returns 2
# 
# -col_index('AA') returns 27



