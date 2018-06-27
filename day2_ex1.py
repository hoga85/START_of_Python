
# coding: utf-8

# In[6]:


import numpy


# In[38]:


data = numpy.loadtxt(".\inflammation-01.csv",delimiter=",")
print("***A bit information on the array:")
print(type(data))
print(data.dtype)
print(data.shape)
print("***What is inside the array:")
print(data)
print("***Let's have a look, what is the first value:")
print(data[0][0])
print("***this is worth noting that the index of python starts from 0, which is annoying...")
print("***Let's have another look, the value at [30][20]:")
print(data[30][20])
print("***Now we can try to select a range of data, first 5 rows and 11 columns:")
print(data[0:4,0:10])


# In[50]:


print("***further divide the data ***")
small = data[0:2,37:39]
print("small is:")
print(small)


# In[51]:


doubledata = data*2
tripledata = data*3
print("original data:",data[:3,36:])
print("doubled data:", doubledata[:3,36:])
print("triple data:", tripledata[:3,36:])


# In[56]:


print("Can we take the average of the whole data set? surely we can:")
print(data.mean())
print("How about we just take the mean of the first row:")
print(data[:1,:].mean())


# In[60]:


### can we obtain the current time? ###
import time


# In[59]:


print(time.ctime())


# In[65]:


### assign multipule variables at the same time ###
maxval,minval,stdval = numpy.max(data),numpy.min(data),numpy.std(data)
print("maxval",maxval,"\n","minval",minval,"\n","stand deviation",stdval)


# In[72]:


### dive in the data in the dataset ###
patient_0 = data[0,:]
print("max inflammation for patient(0):", patient_0.max())
print("max inflammation for patient(1)", numpy.max(data[1,:]))
print("max inflammation for patient(2)", numpy.max(data[2,:]))


# In[87]:


### more about the mean fuction ##
mean_row = numpy.mean(data,axis=1) ## aveage data in each row.
mean_column = numpy.mean(data,axis=0) ## aveage data in each column. 
print(mean_row.shape)
print(mean_column.shape)


# In[89]:


### plot a graphs ###
import matplotlib.pyplot


# In[93]:


### cool function, convert a set of data to an image ###
image = matplotlib.pyplot.imshow(data)
matplotlib.pyplot.show()


# In[94]:


ave_inflammation = numpy.mean(data, axis = 0)
ave_plot = matplotlib.pyplot.plot(ave_inflammation)
matplotlib.pyplot.show()


# In[98]:


max_plot = matplotlib.pyplot.plot(numpy.max(data,axis = 0))
matplotlib.pyplot.show()


# In[120]:


min_plot = matplotlib.pyplot.plot(numpy.min(data,axis = 0))
matplotlib.pyplot.show()


# In[116]:


#### now we can group different plots with the function of (matplotlib.pyplot.figure()) ####
### create an canvus ###
fig = matplotlib.pyplot.figure(figsize=(10,3))
### first plot ###
axes1 = fig.add_subplot(1,3,1)
axes1.set_ylabel("average")
axes1.plot(ave_inflammation)
### second plot ###
axes2 = fig.add_subplot(1,3,2)
axes2.set_ylabel("max") 
axes2.plot(numpy.max(data,axis = 0))
### third plot ###
axes3 = fig.add_subplot(1,3,3)
axes3.set_ylabel("min") 
axes3.plot(numpy.min(data,axis = 0))
### plotting style ###
fig.tight_layout()
matplotlib.pyplot.show()
        


# In[129]:


#### About Loop in Python ####

##First scenario: if we don't use loop, it can be tedious to complete a task ###
word = "lead"
print(word[0],"\n",word[1],"\n",word[2],"\n",word[3])


# In[139]:


##Complete the above task with for loop ###
word = ["a","b",4,6,"Hi"]
for i in word:
    print(i)


# In[149]:


# This is something new for me, the i can be something other than a number ##
length = 0
for vowels in "aeiou":
    length = length +1
    print("The ",length," vowels is", vowels)
## the indent matters!
## the for loop does not end by any command, but it ends when the indent is taken away.
print("There are overall",len("aeiou"),"vowels")


# In[154]:


### List in Python (square bracket) ###
odds = [1,3,5,7]
print("odds are:",odds)
print("The first and last elements in odds are:", odds[0],"and",odds[-1])


# In[156]:


### the taste of for loop is a bit different from R
### it makes more sense to name i with number instead of i,
### as number is assigned by odds[0], odds[1].... 
for number in odds:
    print(number)


# In[159]:


names = ["a","b","c"]
print("names:",names)
names[1] = "Darwin"
print(names)
names[1] ="again"
print(names)


# In[165]:


salsa = ["peppers","onions","cilantro","tomatoes"]
my_salsa = salsa
salsa[0] = "Hot peppers" #### VERY important, the later change affect the previous defined variable ####
print("The ingredients in my salsa:",my_salsa)

## to avoid the above situation ##
my_salsa = list(salsa)
salsa[0] = "Very Hot peppers" #### the memory of my_salsa is new, is nothing to do with salsa now. ####
print("The ingredients in my salsa:",my_salsa)


# In[179]:


x = [["pepper","zucchini","onion"],
     ["cabbage","lettuce","garlic"],
     ["ginger","cucumber","egg"]]
print(x)


# In[187]:


# add an element to the end of an array
odds = [1,3,5,7,11]
odds.append(13) 
odds.append(17)
print("odds after append", odds)
odds.reverse()
print("odds after reverse", odds)


# In[190]:


# add an element to the end of an array
odds = [1,3,5,7,11]
primes = list(odds) ## to avoid changing the odds, after changing primes, we apply list ###
primes.append(13)
print(primes)
print(odds)


# In[191]:


###################
### new library####
###################
import glob


# In[196]:


### the function of glob allows you to search the filenames that contains the specific key words ###
print(glob.glob("inflammation*.csv")) 


# In[197]:


### feel a bit messy about the result, you can sort the files with their names 
print(sorted(glob.glob("inflammation*")))


# In[205]:


## to make the above practice useful, we can save the result to a vairable, FILENAME ##
filenames = sorted(glob.glob("inflammation*"))
filenames = filenames[0:2] ## note there are only 3 filenames, which are filename[0] [1] [2]

for filenames in filenames:
    data = numpy.loadtxt(fname = filenames, delimiter=",")
    ### create an canvus ###
    fig = matplotlib.pyplot.figure(figsize=(10,3))
    ### first plot ###
    axes1 = fig.add_subplot(1,3,1)
    axes1.set_ylabel("average")
    axes1.plot(ave_inflammation)
    ### second plot ###
    axes2 = fig.add_subplot(1,3,2)
    axes2.set_ylabel("max") 
    axes2.plot(numpy.max(data,axis = 0))
    ### third plot ###
    axes3 = fig.add_subplot(1,3,3)
    axes3.set_ylabel("min") 
    axes3.plot(numpy.min(data,axis = 0))
    ### plotting style ###
    fig.tight_layout()
    matplotlib.pyplot.show()
    #matplotlib.pyplot.savefig(fig)   ### not working at the moment
    #help(matplotlib.pyplot.savefig)

