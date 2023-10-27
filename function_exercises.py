# Q1)Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.


def is_two(x):
    "function accepts either no 2 or string 2"
    if x==2 or x=='2':
        
        return True
    else:
        
        return False

#example by function call


is_two(2)


is_two(3)

# is_two() ## to check "shift+tab"

#is_two? ## to view docstrings

# Q2)Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

## 1st way
def is_vowel(x):
    if x in ['a','e','i','o','u']:
        return True
    else:
        return False

is_vowel('i')

is_vowel('b')

## 2nd way
def is_vowel(x):
    vowels='AEIOUaeiou'
    return x in vowels

is_vowel('a')

is_vowel('b')

# Q3)Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

def is_consonant(x):
    
    return not is_vowel(x)

is_consonant('b')

is_consonant('a')

# Q4) Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

def capital_word(word):
    if is_consonant(word[0]):
        return word.capitalize()
    return word

capital_word('codeup')

capital_word('apple')

# Q5)Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(tip_percent,bill): # tip_percent & bill are parameters
    if 0<=tip_percent<=1:
        tip_amount=tip_percent*bill
        return tip_amount
    else:
        return "Invalid tip %"
    

calculate_tip(0.39,20)

calculate_tip(1.5,20)

# Q6) Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

def apply_discount(price,discount_percent):
    if 0<=discount_percent<1:
        discount=discount_percent*price
        price=price-discount
        return price
    else:
        return 'Invalid discount %'
    

apply_discount(20,0.05)

apply_discount(20,1.5)

# Q7) Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.


def handle_commas(string):
    return float(string.replace(",",""))

handle_commas('20,000')

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

get_letter_grade(55)

get_letter_grade(99)

# Q9) Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def remove_vowels(string):
    new_string=" "
    
    for x in string:
        if x not in "AEIOUaeiou":
            new_string +=x
        
        else:
            pass
    return new_string
            

remove_vowels("hello")

# Q10) Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:

#- anything that is not a valid python identifier should be removed
#- leading and trailing whitespace should be removed
#- everything should be lowercase
#- spaces should be replaced with underscores
#- for example:
        
 #       - Name will become name
        
  #      - First Name will become first_name
        
#     - % Completed will become completed

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



    

normalize_name("Name")

normalize_name("first name")

normalize_name("% Completed")

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

normalize_name('& $ k cHA')

normalize_name("First_Name")

normalize_name("% Completed")


# Q11) Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.

 #       -cumulative_sum([1, 1, 1]) returns [1, 2, 3]
  #      -cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]


def cumulative_sum(num):
    for x in range(len(num)):
        if x !=0:
            num[x]=num[x]+num[x-1]
    return num

cumulative_sum([1, 1, 1])

cumulative_sum([1, 2, 3, 4])







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











