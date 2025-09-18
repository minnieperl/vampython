#we have to use if else condition for decision making in python 
#check you are eliglible for voting or not
#get the age from user
userage=int(input("enter your age"))
# to check the user is eligible for voting then check age must be greater than 18

if userage>18:
    print("you'r eligible for voting ")
else:
    print("you'r not eligible for voting ")

#check the user is eligibal for vote and super  vote
#super vote age should be greater than 55
#vote age should be greater than 18 less than 55

if userage > 18:
    print(" you'r eligibale for voting")
elif userage > 55:
    print(" you'r eligibale for supervote ")
else:
    print("you'r not eliglible for voting")    