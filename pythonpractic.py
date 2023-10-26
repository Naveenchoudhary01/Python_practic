# ---------------------str---------------------------
# a = 'NaVeEn,1,2.0'                 #strnig ,int, float,
# print(a)
# a="NaVeEn"                         # for convert lower case
#b=a.lower()
#print(b)
# print(a.lower())
# b=a.upper()                        # for convert upeer case
# print(b)
# print(a[::-1])                     # for reverse str
# a='apple','banana','apple','mango' # count particuller elements
# print(a.count('apple')) 
#  print(sum(a))                    # sum of list
# --------list-------------------
# a=['naveen',1,2,3,1.0,2.0]         #list can modified
# print(a)
# print(a[0])                        # to get item
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
# print(len(a))                      # to get length
# # to get any 2to 5 char
# print(a[2:5])
# a[1]='vikas'                       #apend
# print(a)
# a=input('enter the name:')         #take input from user
# print(a)
# a='Naveen'
# print(len(a))                      #length
# for i in a:                        # itrate str from loop
#   print(i)
# print(a.endswith('n'))             #true
# print(a.startswith('N'))           # false
# print(a.count('e'))                # count prticuler aliments
# a='naveen kumar'
# print(a.capitalize())              #capital first latter
# print(a.find('e'))                 # find the word indexing in str
# print(a.find('v'))
# print(a.replace('naveen', 'navin' )) #replace word

# ----------------------list-----------------mutable----------------------
# a=['naveen','kumar','vikas']      #reverse list
# a.reverse()
# print(a)
# a.append('singh')                 #apend elements
# print(a)
# a.remove('kumar')                 # remove  elements
# print(a)
# a=['naveen','kumar',1,2,3,4,5,]   # list indexing
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
# print(a[5])
# print(a[6])
# a.append("singh")                 # apend new elements in list
# print(a)
# a.remove(4)                       #remove  elements
# print(a)
# a.clear()                         #clr list all elements
# print(a)
# b=['singh',9,8,7,6]
# a.extend(b)                       # extends list
# print(a)
# a = ['naveen', 'kumar', 1, 2, 3, 4, 5, ]
# a.insert(2, 'singh')
# print(a)
# a.pop(1)                          # delete particuller items from index
# print(a)
# a.remove(2)                       # remove particuller item from name
# print(a)
# a.reverse()                       # list reverse
# print(a)
# a.sort()                          # only work with str upper case sort to first index
# print(a)
# mylist = ["a", "b", "a", "c", "c"]
# mylist = list(dict.fromkeys(mylist))   # remove duplicatte from list
# print(mylist)
# a=[1,2,3,4,1,3,5,4]
# b=list(dict.fromkeys(a))
# print(*set(a))
# ----------------------dict-----------------------------
# dict={                            # get value from dict
#  'naveen':'singh',
#  'amit':'kumar',
#  'ravi': 'rana' }
# print(dict['naveen'])
#--------------------------------------------------
# dict={}                           # take unput from user create dict
# a= int(input('enter the elements :'))
# for i in range(a):
#      b= input('enter the key :')
#      c= input('enter the value :')
#      dict.update({b:c})
#      print(dict)
#--------------------------------------------
# a = (input('enter the key :')) 
# dict={
#     '100':"naveen",
#     '101':"sonu",
#     '102':"ravi",
#     '103':"sumit",
#     '104':'amit'}
# print(dict[a])
# dict['100'] = 'kumar'            # for chanage elements
# print(dict)
# dict.update({'105':'kumar'})     # for update  elements
# print(dict)
# dict.pop('104')                  # for delte any elements
# print(dict)
# for dict in dict.items():        # use loop in dict
#     print(dict)
# child1 = {                       # nested dict
#     "name": "Emil",
#     "year": 2004}
#         child2 = {
#                 "name": "Tobias",
#                 "year": 2007}
#                     child3 = {
#                         "name": "Linus",
#                         "year": 2011}
#                               myfamily = {
#                                   "child1": child1,
#                                   "child2": child2,
#                                    "child3": child3}
# print(myfamily)
# dict = {
#         '100':"naveen",
#         '101':"sonu",
#         '102':"ravi",
#         '103':"sumit",
#         '104':'amit'
#     }
# a=dict.keys()                     # get keys only
# b=dict.values()                   # get value only
# print(a)
# print(b)
# -------------tuple-------immutable----------
# tup=(1,0,3,2,5,6,7,8,9,10,1,2,3,2,1,2,4,5,6)
# a=tup.count(2)                   # count perticuler elements
# print(a)
# a=tup.__len__()                  # to get len of tup
# print(a)
# a=tup.index(0)                   # for indexing
# print(a)
# ----------sets--------unorderd------
# a={'naveen','kumar','singh'}
# a.add('vikas')                   # for adding  a new elements
# print(a)
# a.remove('naveen')               # for remove a elements
# print(a)
# a = {'naveen', 'kumar', 'singh'}
# b = {"google", "microsoft", "apple"}
# a.update(b)                      # for update 2 or more sets and combind
# print(a)
# --------------------LOOPS----------------------------
# while loop
# a=0
# while a<10:
#     print('hello naveen')
#     a=a+1
#------------------------------------------
# a=0
# while True:                   # infinite loop
#     print('naveen')
#     a=a+1
#---------------------------------------
# for loop
# for i in range(0,100):              # range fun
#     print(i)
#------------------------------------
# a='Naveen'
# for i in a:
#     if i=='e':
#         break                        # break stmt
#     print(i)
#----------------------------------------------
# a='Naveenkumar'
# for i in a:
#     if i=="n":
#         continue                      # continue stmnt
#     print (i)


#------------------------------------------------------
# def find_max(nums):
#     max_num = float("-inf")      # smaller than all other numbers
#     for num in nums:
#         if num > max_num:
#          max_num=num
#     return max_num
# a = print("Hello", end=' ')
# print(a)
# ---------file methods-----------------------------
# import webbrowser
# webbrowser.open_new('chini.pdf')  # open pdf 
# a = open('naveen.txt', 'r')      # read  or close file
# print(a.read())
#a.close()
# a=open('naveen.txt','r')
# print(a.fileno())                #file no
# a=open('naveen.txt','a')
# a.write('i m writing another line in my file')  # write in file
# a.flush()                                       #flush the data in file
# a=open('naveen.txt','r')
# print(a.isatty())                # return type bool vale
# a=open('naveen.txt','r')
# print(a.readable())              # if file readble return true  else false
# print(a.readline())              # read first line of file
# print(a.readlines())             # return as a list of file
# print(a.seek(4))                 # change file position
# print(a.seekable())              # true if seekable else false
# a.readline()
# print(a.tell())                  # current file postion after reading first line
# a.truncate                       # resize the file
# a=open('naveen.txt','a')
# print(a.writable())              # true if writable else false
# a.writelines(['this is my new line '])  # write line in list \n for new line

# li=['a','b','c']
#                  #.join keywords
# print('d'.join(li))
# import os
# os.remove('naveen.txt')          # for remove file 
# os.rmdir('foldername')           # delete folder
#---------------numpy--------------------------------------------
# import numpy         # numpy is a python librarary working with arrys
# a=numpy.array([1,2,3,4,5,6,7,8,9,10 ]) # 1-D array
# print(a)
# print(type(a))                     # type of array
# a=numpy.array((1,2,3,4,5,6,7,8,9,10)) # use a tupple to cerate array
# print(a)
# a=numpy.array([[1,2,3,4,5], [6,7,8,9,10]])  #2-D array
# print(a)
# print(a.ndim)                      # typee of 2-D array
# a=numpy.array([[[1,2,3],[4,5,6],[7,8,9]]]) #3-D arrays
# print(a)
# print(a.ndim)
# a=numpy.array([1,2,3,4,5], ndmin=5 # to make dimensional array
# print(a)
# a=numpy.array([1,2,3,4,5])  
# print(a[0])                         # acceess arrray elements
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
# print(a[::-1])                      # reverse array
# a=numpy.array([[1,2,3,],[4,5,6]])   # acceess 2-D array elemenst
# print(a[1,0])
# a=numpy.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])
# print(a[0,1,2])                     # access 3-D array elemets
# a=numpy.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(a[1,-2])                      # negative indexing
# a=numpy.array([1,2,3,4,5,6,7,8,9,10])
# print(a[0:5:])    # start:step:end  # slicing array
# print(a[1:])
# print(a[::9])
# a=numpy.array([1,2,3,4,5,6,7])      # negative slicing array
# print(a[-5:-1]) 
# a=numpy.array([[1,2,3,4],[5,6,7,8]])    
# print(a[0:2,1:3])                   # access 2-D array
#------------------Data type in numpy-------------------------------
# i - integer                         # numpy has some extra data type
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type(void)
# import numpy
# a=numpy.array([1,2,3,4,5])                    #int
# b=numpy.array(['aAa','bBb','cCc','dDd'])      
# print(a.dtype)
# print(b.dtype)


