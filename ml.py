#mean - it is average od data set 
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd
dataset=[70,90,65,60,80,60]
mean=np.mean(dataset)
print("mean is :",mean)

# meadian - mid value of data set 
median=np.median(dataset)
print("medain is :",median)

from scipy import stats
#dataset1=[70,90,65,60,80,60]
mode=stats.mode(dataset)
print("mode is :",mode)

#maximum data set 
max=np.max(dataset)
print("maximum data :",max)

#minimun data set 
min=np.min(dataset)
print("minimum data :",min)

#standard deviation (SD)-
st=np.std(dataset)
print("standard devaition is :",st)

#standard devaition is the square root of variance 

#variance - 
var=np.var(dataset)
print("variance is :",var)

# unifrom distribution - it's a technique to arrange the data in order 
unifromdata=np.random.uniform(1,10,500)
print(unifromdata)
plt.hist(unifromddata)


# normal distribution -
normaldata=np.random.normal(1,10,500)
print(normaldata)

#y= refreance , m= dataset ,x=marks ,c=hours study 
#y=mx+c