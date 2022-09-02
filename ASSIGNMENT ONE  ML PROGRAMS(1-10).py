#!/usr/bin/env python
# coding: utf-8

# In[10]:


ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]#initialisation of list
print(min(ages),max(ages))#function for finding minimum and maximumages
ages.append(19)#function for adding number to the list
ages.append(26)#function for addding number to the list
print(ages)#function for finding list
import statistics
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24, 19, 26]
print("Median of data-set is : % s " % (statistics.median(ages)))#function for finding median of ages
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24, 19, 26]
avg = sum(ages)/len(ages)
print("The average is ", round(avg,2))#function for finding average of ages
x = range(19,27)
for n in x:
    print(n)#Printing range of ages


# In[14]:


dog={} #function for creating empty dictionary
dog['name']= 'bull dog'#function for adding name 
dog['color']= 'black'#function for adding colour
dog['breed']= 'american breed'#function for adding breed
dog['legs']=4 #function for adding legs
dog['age']=10 #function for adding age
print(dog)


student=dict() #function for creating dictinory
student['first_name']='lucky'
student['last_name']= 'great'
student['gender']='Male'
student['age']=21
student['Marital_status']='No'
student['skills']=['C','c++','Python']
student['country']='India'
student['city']='banglore'
student['address']= 'xyz colony'
print(student) ##function for printing student dictinory
len_of_student= len(student)
print(len_of_student)# #function for printing lenth of student dictinory
skills_of_student= student.get('skills')
print(skills_of_student)
print(type(skills_of_student))#function for printing skills of student
student.update({'skills':['C','c++','Python','java','cobal']})
print(student)
student_keys= list(student.keys())
print(student_keys)#function for printing student keys
student_values= list(student.values())
print(student_values)#function for printing student values




# In[8]:


sisters=('ammu','bhavi','sweety')#creating a tuple
brothers=('rahul','mahi','sai')
siblings= sisters+ brothers#joining sister_tuple and brother_tuple using addition operator
print(siblings)
siblings_count=len(siblings)#function for getting length of the siblings
print(siblings_count)
temp_siblings=list(siblings)#using temp function 
temp_siblings.extend(['raki','leon'])#using extend function 
family_members=tuple(temp_siblings)
print(family_members)#printing family members to get a list


# In[12]:


it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
len_of_it=len(it_companies)#using length function
it_companies.add('Twitter')
print(it_companies)#using print function to get the list of it companies
it_companies.update({'wipro','infosys','Tesla'})
print(it_companies)
it_companies.remove('Microsoft')#using remove function
print(it_companies)
#The built-in method, discard () in Python, removes the element from the set only if the element is present in the set. If the element is not present in the set, then no error or exception is raised and the original set is printed.
A = {19, 22, 24, 20, 25, 26}#intilializing sets
B = {19, 22, 20, 25, 26, 24, 28, 27}

C=A.union(B)
print(C)
A_inter_B= A.intersection(B)
print(A_inter_B)
subset_check= A.issubset(B)
print(subset_check)
#As the function is subset() return true A is a Subset of B)
disjoint_check= A.isdisjoint(B)
print(disjoint_check)

E=A.union(B)
D= B.union(A)
print(E)
print(D)
#using delete function to delete the sets
del A 
del B
del C
del D
del E
age = [22, 19, 24, 25, 26, 24, 25, 24]
len_age=len(age)
age_set=set(age)
len_age_set=len(age_set)
diff_age= len_age-len_age_set
print(diff_age)
                



# In[20]:


print('Name   \tAge\tCountry\tCity')
print('Asabeneh  250\tFinland\tHelsinki') #using \t that using tab space to print the input in given format


# In[24]:


lb_kg_conversion= 0.45359237 #using lb to kg conversion 

N=int(input('enter the number of students'))
L1=[]

for i in range(N):#running for loop from 0 to n that is number of students
    L1.append(int(input('enter the element ')))
    
output=[lb_kg_conversion*i for i in L1 ]
print(output)
    


# In[8]:


phi = 3.14
g=30
radius = float(input())

def Area(r):# using def function for defining area
	_area_of_circle_ = phi * r**2
	print("Area of the given radius is %s" %_area_of_circle_)#using print function to get the area of given radius
Area(radius)

def circumferance(t):using def function for defining circumferance
    _circum_of_circle_ = 2 * phi *t
    print("circumferance",_circum_of_circle_)
circumferance(radius)
Area(g)
circumferance(g)


# In[11]:


str="I am a teacher and I love to inspire and teach people"
print(type(str)) #using type function to get the data
y=str.split() #using split function for spliting the words
print(y)
set_str=set(y) #adding the split words into set
print(set_str)
print("no:- of unique words in given sentence is %s" % len(set_str)) #as set doesnt take duplicate keys we can directly find the length


# In[13]:


radius=10
area=3.14*radius**2#using area formula to get the req value
sentence="The area of a circle with radius {} is {} meters square.".format(radius,int(area))
print(sentence)


# In[ ]:




