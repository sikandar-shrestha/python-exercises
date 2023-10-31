#!/usr/bin/env python
# coding: utf-8

# ## Q1) Import and test 3 of the functions from your functions exercise file. Import each function in a different way:
# 
# a) Run an interactive python session and import the module. Call the is_vowel function using the . syntax.
# 
# 
# b) Create a file named import_exercises.py. Within this file, use from to import the calculate_tip function directly. Call this function with values you choose and print the result.
# 
# 
# c) Create a jupyter notebook named import_exercises.ipynb. Use from to import the get_letter_grade function and give it an alias. Test this function in your notebook.
# 
# 
# Make sure your code that tests the function imports is run from the same directory that your functions exercise file is in.

# In[ ]:


import function_exercises as fe


# In[ ]:


# once you alias a python file(*.py) import, it can only be called back by that that alias

fe.calculate_tip(0.15,85)


# In[ ]:


fe.get_letter_grade(90)


# In[ ]:


fe.get_letter_grade(95)


# In[ ]:


fe.get_letter_grade(50)


# ##Q2) Read about and use the itertools module from the python standard library to help you solve the following problems. Note: Many of these functions in this library return an object, to see the results of the function, cast this object as a list.
# 
# - How many different ways can you combine a single letter from "abc" with either 1, 2, or 3?
# - How many different combinations are there of 2 letters from "abcd"?
# - How many different permutations are there of 2 letters from "abcd"?

# In[ ]:


import itertools as its


# In[ ]:


#How many different ways can you combine a single letter from "abc" with either 1, 2, or 3?
list(its.product('abc','123'))


# In[ ]:


# Another way:-

list(its.product('abc',[1,2,3]))


# In[ ]:


len(list(its.product('abc','123')))


# In[ ]:


len(list(its.product('abc',[1,2,3])))


# In[ ]:


#How many different combinations are there of 2 letters from "abcd"?
list(its.combinations('abcd',2))


# In[ ]:


len(list(its.combinations('abcd',2)))


# In[ ]:


#How many different permutations are there of 2 letters from "abcd"?
list(its.permutations('abcd',2))


# In[ ]:


len(list(its.permutations('abcd',2)))


# Q3) Save this file as profiles.json inside of your exercises directory (right click -> save file as...).
# 
# Use the load function from the json module to open this file.
# 
# 
# import json
# 
# json.load(open('profiles.json'))
# 
# 
# Your code should produce a list of dictionaries. Using this data, write some code that calculates and outputs the following information:
# 
# 
# 
# 
# 
# -Total number of users
# 
# -Number of active users
# 
# -Number of inactive users
# 
# -Grand total of balances for all users
# 
# -Average balance per user
# 
# -User with the lowest balance
# 
# -User with the highest balance
# 
# -Most common favorite fruit
# 
# -Least most common favorite fruit
# 
# -Total number of unread messages for all users

# In[ ]:


import json


# In[ ]:


# storing in variable for future use

data=json.load(open('profiles.json'))
data


# In[ ]:


# Another way to Load the data from the JSON file
'''
with open('profiles.json', 'r') as file:  # r=read mode
    data = json.load(file)
'''

# your code should produce a list of dictionaries. Using this data, write some code that calculates and outputs the 
# following information:

data[0]




# In[ ]:


# how to access a list
my_list=[1,2,3,4]

# subsetting only 1st to 3rd values non-inclusive
my_list[0:2]


# In[ ]:


# how to access a dictionary
my_dict={'a':0,'b':23,'c':4}

# indexing by the key
my_dict['b']


# In[ ]:


# access a list of dictionaries
lst_dict = [{'name':'Mark', 'age':29}, {'name':'Eliza Thronberry', 'age':34}]

# only returns first dictionary
# to access mulitple need to use
# a control structure to iterate 
# over the dictionaires
lst_dict[0]


# In[ ]:


# now i can get separate dicitonaries and access their elements individiually
for dictionary in lst_dict:
    print(dictionary['name'], dictionary['age'])


# ## 3)i)Total number of active users

# In[ ]:


# Total number of active users
len(data)


# # 3) ii)Number of active users

# In[ ]:


# Number of active users
active_list=[]
for x in data:
    if x["isActive"]==True:
        active_list.append(x["name"])
len(active_list)


# In[ ]:


# another way
count=0
for x in data:
    if x['isActive']==True:
        count +=1
count


# # 3) iii) number of inactive users

# In[ ]:


# number of inactive users
inactive_list=[]
for x in data:
    if x["isActive"]==False:
        inactive_list.append(x["name"])
len(inactive_list)


# In[ ]:


# another way:-
count=0
for x in data:
    if x['isActive']==False:
        count +=1
count


# ## 3) iv) grand total of balances for all users

# In[ ]:


# for example
data[0]['balance']


# In[ ]:


# grand total of balances for all users
# 1st method (by using string methods):-

grand_total=0
for x in data:
    balance=float(x["balance"].replace('$','').replace(',','')) # casting to float to keep decimal precision
    grand_total +=balance

print("grand total of balances:",round(grand_total,2))
    


# In[ ]:


# another way (by importing user defined function):-

import importlib # make adjustments to functions without restarting kernel
import function_exercises as f

# just to make adjustments to my function without restarting kernel
importlib.reload(f)

grand_total = 0

for x in data:
    # utilizing pre defined functions
    grand_total += f.handle_commas(x['balance'].strip('$'))
    
grand_total










# ## 3) v) average balance per user

# In[ ]:


# average balance per user
average_balance=grand_total/len(data)
round(average_balance,2)


# ## 3) vi & vii ) user with the lowest & highest balance

# In[ ]:


## user with the lowest balance

# create a list of all balaces
balance_list=[float(x['balance'].strip('$').replace(',','')) for x in data]
balance_list


# In[ ]:


# another way to find balance list:-

balance_list=[]
for x in data:
    bal=float(x["balance"].strip("$").replace(",",""))
    balance_list.append(bal)
balance_list


# In[ ]:


min_bal=min(balance_list)
max_bal=max(balance_list)
print("lowest balance:",min_bal)
print("highest balance:",max_bal)


# In[ ]:


# Another way
# user with minimum balance
for x in data:
    clean_balance=float(x["balance"].strip('$').replace(',','')) #striping out string characters
    if clean_balance==min_bal:
        print(x['name'],clean_balance)


# In[ ]:


# Another way
# user with highest balance
for x in data:
    clean_balance=float(x["balance"].strip('$').replace(',','')) #striping out string characters
    if clean_balance==max_bal:
        print(x['name'],clean_balance)


# ## 3) viii & ix ) Most & least  common fruit

# In[ ]:


# dictionary way


favorite_fruit_count = {}
for x in data:
    fruit = x['favoriteFruit']
    if fruit in favorite_fruit_count:
        favorite_fruit_count[fruit] += 1
    else:
        favorite_fruit_count[fruit] = 1
print(f' common favorite fruit: {favorite_fruit_count}')







# In[ ]:


# most common favorite fruit
most_common_favorite_fruit=max(favorite_fruit_count,key=favorite_fruit_count.get)
print(f'most common fav fruit:-- {most_common_favorite_fruit}')


# In[ ]:


# least most common favorite fruit
least_common_favorite_fruit=min(favorite_fruit_count,key=favorite_fruit_count.get)
print(f'least common fav fruit:-- {least_common_favorite_fruit}')


# In[ ]:


# Another way:-
# empty list to add to

fruit_ls=[]

for x in data:
    
    fruit_ls.append(x['favoriteFruit'])
fruit_ls


# In[ ]:


# turn list into set to only return unique values
set(fruit_ls)


# In[ ]:


# more manual way to calculate most & least common favorite fruit
fruit_ls.count('apple')


# In[ ]:


fruit_ls.count('banana')


# In[ ]:


fruit_ls.count('strawberry')


# In[ ]:


# coming soon way using pandas library
import pandas as pd

# converting to series
fruit_ls = pd.Series(fruit_ls)

fruit_ls.value_counts()


# In[ ]:





# ## 3) x ) total number of unread messages for all users

# In[ ]:


# 1st method:-
total = 0
for x in data:
    index_begin = x["greeting"].find("have")
    index_end = x["greeting"].find("unread")
    num = int(x["greeting"][index_begin+5:index_end])
    total += num
total






# In[ ]:


## 2nd method:-

def extract_digits(s):
    return int("".join([c for c in s if c.isdigit()]))

greetings = [x['greeting'] for x in data]
sum([extract_digits(greeting) for greeting in greetings])


# In[ ]:


data[0]['greeting'].split(' ')


# In[ ]:


## 3rd method:-


# empty var to add ints to
total_unread = 0

# looping over individual profiles
for x in data:
    # storing split message greeting in a variable
    message = x['greeting'].split()
    
    # loop over split message and look for digits to add to total_unread
    for word in message:
        
        # checking if word is a digit
        if word.isdigit():
            word = int(word) # casting to int for math calculations
            total_unread += word
            
total_unread


# ## BQ1) find out how many total unique tags there are for all users?

# In[ ]:


unique_tags=set()
for x in data:
    user_tags=x.get("tags",[])
    unique_tags.update(user_tags)
total_unique_tags=len(unique_tags)
print("total unique tags:",total_unique_tags)
    


# ## BQ2) Display a user's name and all of their respective friends.

# In[ ]:


def users_their_friends(x_name,data):
    for x in data:
        if x.get("name")==x_name:
            print(f"{x_name}/'s frineds:")
            for x_friends in x.get("friends",[]):
              print(x_friends)  


# In[ ]:


users_their_friends('Hebert Estes',data)


# In[ ]:


users_their_friends('Ewing Larson',data)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




