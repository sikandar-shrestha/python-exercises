#!/usr/bin/env python
# coding: utf-8

# In[1]:


import importlib





import function_exercises as fa


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




fa.calculate_tip(0.15,85)





fa.get_letter_grade(90)





fa.get_letter_grade(95)





fa.get_letter_grade(50)


# ##Q2) Read about and use the itertools module from the python standard library to help you solve the following problems. Note: Many of these functions in this library return an object, to see the results of the function, cast this object as a list.
# 
# - How many different ways can you combine a single letter from "abc" with either 1, 2, or 3?
# - How many different combinations are there of 2 letters from "abcd"?
# - How many different permutations are there of 2 letters from "abcd"?



import itertools as its





#How many different ways can you combine a single letter from "abc" with either 1, 2, or 3?
list(its.product('abc','123'))





len(list(its.product('abc','123')))





#How many different combinations are there of 2 letters from "abcd"?
list(its.combinations('abcd',2))





len(list(its.combinations('abcd',2)))





#How many different permutations are there of 2 letters from "abcd"?
list(its.permutations('abcd',2))





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
# Total number of users
# 
# Number of active users
# 
# Number of inactive users
# 
# Grand total of balances for all users
# 
# Average balance per user
# 
# User with the lowest balance
# 
# User with the highest balance
# 
# Most common favorite fruit
# 
# Least most common favorite fruit
# 
# Total number of unread messages for all users




import json
json.load(open('profiles.json'))





import json

# Load the data from the JSON file
with open('profiles.json', 'r') as file:  # r=read mode
    data = json.load(file)



# Total number of active users
len(data)




# Number of active users
active_list=[]
for x in data:
    if x["isActive"]==True:
        active_list.append(x["name"])
len(active_list)





# number of inactive users
inactive_list=[]
for x in data:
    if x["isActive"]==False:
        inactive_list.append(x["name"])
len(inactive_list)





# grand total of balances for all users

total_bal=0
for x in data:
    bal=float(x["balance"].replace('$','').replace(',',''))
    total_bal +=bal

(round(total_bal,2))
    





# average balance per user
average_balance=total_bal/len(data)
average_balance





# user with the lowest balance

def handle_balance(s):
    return float(s.replace(',', '').strip('$'))

user_with_the_lowest_balance = data[0]['balance']
for x in data[1:]:
    if handle_balance(x['balance']) < handle_balance(user_with_the_lowest_balance):
         user_with_the_lowest_balance = x['balance']
user_with_the_lowest_balance







#user with the highest balance

def handle_balance(s):
    return float(s.replace(',', '').strip('$'))

user_with_the_highest_balance = data[0]['balance']
for x in data[1:]:
    if handle_balance(x['balance']) > handle_balance(user_with_the_lowest_balance):
         user_with_the_lowest_balance = x['balance']
user_with_the_highest_balance











# common favorite fruit


favorite_fruit_count = {}
for x in data:
    fruit = x['favoriteFruit']
    if fruit in favorite_fruit_count:
        favorite_fruit_count[fruit] += 1
    else:
        favorite_fruit_count[fruit] = 1
print(f' common favorite fruit: {favorite_fruit_count}')










# most common favorite fruit
most_common_favorite_fruit=max(favorite_fruit_count,key=favorite_fruit_count.get)
print(f'most common fav fruit:-- {most_common_favorite_fruit}')





# least most common favorite fruit
least_common_favorite_fruit=min(favorite_fruit_count,key=favorite_fruit_count.get)
print(f'least common fav fruit:-- {least_common_favorite_fruit}')





# total number of unread messages for all users
total = 0
for x in data:
    index_begin = x["greeting"].find("have")
    index_end = x["greeting"].find("unread")
    num = int(x["greeting"][index_begin+5:index_end])
    total += num
total









## Another way

def extract_digits(s):
    return int("".join([c for c in s if c.isdigit()]))

greetings = [x['greeting'] for x in data]
sum([extract_digits(greeting) for greeting in greetings])







