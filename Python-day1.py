#!/usr/bin/env python
# coding: utf-8

# # Python
# - Topics covered
#   - Operators
#   - Datatypes
#   - Conditional statements

# # Python
# - Topics covered
#   1. Operators
#   2. Datatypes
#   3. Conditional statements

# **Python** 
# *Python*
# ***Python***

# In[ ]:


print("Gitam")
print("Gitam")
print("Gitam")


# In[4]:


print("Sripath",end=' @ ')
print("gmail")


# In[5]:


a=10
print(a)
a*2


# In[6]:


b=20
a+b


# In[7]:


name="Gitam"
Address="Hyd"
print(name,"university","Place",Address)


# In[8]:


input("enter your name ")


# In[9]:


b=int(input())
type(b)


# In[10]:


b=input()
type(b)


# In[11]:


x=11
y=12.5
z=x+y;
print(type(x),type(y),type(z))


# In[14]:


c=complex(3,4)
print(c)


# In[15]:


v=complex(1,5)
c


# In[16]:


i=100
print(type(i))
j=str(i)
print(type(j))
k=float(i)
print(type(k))


# In[17]:


a="100"
print(type(a))
b=float(a)
b


# In[28]:


x=6
y=3
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x**y)


# In[33]:


a=10
b=20
print(a>=20 and a>30)
print(a>=10 or a>30)


# In[34]:


x=6
y=3
print(x>y)
print(x<y)
print(x!=y)
print(x==y)
print(x>=y)
print(x<=y)


# In[35]:


str1="sripath"
print('a' in str1)
print('c' in str1)


# In[36]:


a = 33
b = 200
if b > a:
  print("b is greater than a")


# In[37]:


a = 33
b = 22
if b > a:
  print("b is greater than a")
else:
  print("a is greater than b")


# In[38]:


a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
elif a>b:
  print("a is greater than b")


# In[39]:


num=int(input("enter a number"))
if num%2==0:
  print("the number is even")
else:
  print("the number is odd")


# In[40]:


num=int(input("Enter number:"))
if(num%3==0 and num%5==0):
  print("number is divisible by 3 and 5")
else:
  print("Not divisible")


# In[1]:


a = 33
b = 23
c = 45
if a > b and a > c:
  print("a is greater")
elif b > a and b > c:
  print("b is greater")
elif c > a and c > b:
  print("c is greater")


# In[2]:


num=int(input("entre a number:"))
if num==0:
  print("number is zero")
elif num>0:
  print("number is +ve")
elif num<0:
  print("number is -ve")

