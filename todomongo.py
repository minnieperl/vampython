from pymongo import MongoClient   

#to create the mongo db client
client = MongoClient("mongodb://localhost:27017/")

#to create new database in client 
myDb=client["tododb"]

#to create new collection in database
mycol=myDb["dailyTask"]

#to insert the task in tododatabase
mytask={"taskName":"mongoDatabase"}

#to execute the insert in collection
mycol.insert_one(mytask) 