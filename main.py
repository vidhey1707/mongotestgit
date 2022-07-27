
import pymongo

client = pymongo.MongoClient("mongodb+srv://vidhey1707:V!dhey1707@cluster0.f0zz9.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : "Vidhey",
    "email" : "vidhey@gmail.com",
    "mob" : 83498934
}

db1 = client['mongotest']
col = db1['test']
col.insert_one(d)