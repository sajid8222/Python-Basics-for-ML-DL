#!/usr/bin/env python
# coding: utf-8

# In[1]:


first_name='Sajid'
last_name='Alam'


# In[3]:


print("My first name is {} and the last name is {}".format(first_name,last_name))


# In[4]:


print("My first name is {first} and the last name is {last}".format(first=first_name,last=last_name))


# In[5]:


len('sajid')


# In[6]:


type("Sajid")


# In[7]:


type([1,2,3])


# # Python Data structures and Boolean

# - Boolean
# - Boolean and logical Operators 
# - lists
# - Comparison operators
# - Dictionaries 
# - Tuples
# - Sets

# ## Boolean Variables

# Boolean values are the two constant objects False and True
# 
# They are used to represent truth values(other values can also be considered false or true).
# 
# In numeroc contexts (for example, when used as the argumemts to an arithmetic operators), they behave like the integers 0 and 1 respectively.
# 
# They are written as Flase and True, respectively.

# In[9]:


print(True, False)


# In[10]:


bool()


# In[11]:


my_str= "SDN NETWORKING"


# In[13]:


print(my_str.isalnum()) # To check if all char are numbers
print(my_str.isalpha()) #check if all char in the string are alphabetic
print(my_str.isdigit()) #test if string contains digits
print(my_str.istitle()) #test if string contains title words
print(my_str.isupper()) #test if string contains upper case
print(my_str.islower()) #test if string contains lower case
print(my_str.isspace()) #test if string contains spaces
print(my_str.endswith('k')) #test if string endswith a d
print(my_str.startswith('K')) #test if string startswith H


# 
# # Boolean and logical Operattors

# In[14]:


True and True


# In[15]:


True and False


# In[16]:


True or False 


# In[17]:


True or True


# In[18]:


str_example = 'Hello world'
my_str = 'Krish'


# In[19]:


my_str.isalpha() or str_example.isnumeric()


# # SETS
# 
# A Set is unordered collection data type that is iterable, mutable and has no duplicate elements. Python set class repsents the mathematical notion of a set. This is based on data structure known as a hash table.

# In[1]:


set_var = set()
print(set_var)
print(type(set_var))


# In[2]:


set_var = {1,1,2,3,4,5}


# In[4]:


print(set_var) # remove the duplicates


# In[6]:


set_var = {"Avengers","Ironman","Hitman"}
print(set_var)


# In[ ]:


#Inbuilt functions in Sets


# In[9]:


set_var.add("Hulk")
print(set_var)


# In[34]:


set1 = {"Avengers","IronMan","Hitman"}
set2 = {"Avengers","IronMan","Hitman","hulk2"}


# In[21]:


set2.intersection_update(set1)


# In[22]:


set2


# In[36]:


## Difference

set2.difference(set1)


# In[35]:


print(set2)


# In[37]:


## Difference update

set2.difference_update(set1)


# In[38]:


set2


# # Dictionaries
# 
#  A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets and they have keys values.

# In[39]:


dict={}


# In[43]:


type(dict)


# In[44]:


set_ex = {1,2,3,4,5
         }


# In[45]:


type(set_ex)


# In[46]:


## Let create a dictionary

my_dict = {"Car1": "Alto", "Car2": "Mehran", "Car3":"Civic"}


# In[47]:


print(my_dict)


# In[48]:


## Access the item on the values based on keys.

my_dict['Car1']


# In[50]:


# We can loop for each keys

for x in my_dict:
    print(x)


# In[51]:


# We can also loop with each values.
for x in my_dict.values():
    print(x)


# In[53]:


# We can also call both keys and values:\

for x in my_dict.items():
    print(x)


# In[54]:


# Adding items in Dict

my_dict['car4'] = 'Audi 2.0'


# In[55]:


print(my_dict)


# In[57]:


# Replacing Key 1 

my_dict['Car1'] ='Maruti'


# In[58]:


print(my_dict)


# # Nested Dictionary

# In[61]:


car1_model = {'Mercedes'  : 2000}
car2_model = {'Audi'      : 2001}
car3_model = {'Kia'       : 2022}

car_type = {'car1':car1_model, 'car2': car2_model, 'car3':car3_model}


# In[62]:


print(car_type)


# In[67]:


## Accessing the item in the dictionary

print(car_type['car1'])
print(car_type['car2'])
print(car_type['car3'])


# In[72]:


print(car_type['car1']['Mercedes'])
print(car_type['car2']['Audi'])
print(car_type['car3']['Kia'])


# # Tuples ()
# 
# Immuatable 

# In[73]:


## Create an emty tuples

my_tuple =tuple()


# In[74]:


type(my_tuple)


# In[75]:


my_tuple = ("HP","Lenevo","Dell")


# In[76]:


print(my_tuple)


# In[78]:


## inbuilt func

my_tuple.count("Dell")


# In[80]:


my_tuple.count("HP")


# In[ ]:




