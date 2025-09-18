#data type is used to define the data in which form 

#int data is used to store the numeric type of data
# note in python we dont't need to declare the datatype 
# we just assign the value in variable  
#variable can store any type of value with type of data 
age= 33
name = "mukul sharma "
salary= 2599.89

# how to pass the  variables inside the print statement
# we have 3 ways to pass the variable in print statement 
print("my nameis ", name ,"and salary ",salary,"age",age) 
#it generate thee type error reason string only concatenate with string not int
# solution 1:- replace + by , when data type is not string
print ("my name is "+name+"and salary",salary,"and age",age)
#solution 2: pass the variable in print statement with f()
print(f"my name is {name }salalry is {salary } and age {age}")
#solution 3: typecast the data into string
salarystring= str(salary)
agestring= str(age)
print("my name is "+ name+"and salary "+salarystring+"and age"+agestring)

#to find the type od data we need to use type() function
print(type(name))
print(type(age))
print(type(salary))
