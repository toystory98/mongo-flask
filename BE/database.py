import pymongo
from pymongo import MongoClient
import numpy as np

client = MongoClient('mongodb://root:example@localhost:27017')
db = client['test']

def getmonth(station, month, year):
    l = []
    query = db.testfile.find({ "$and" : [{ "month" : int(month) }, { "year" : int(year) } ] } ,{station:1})
#     query = db.testfile.aggregate([
#         { "$replaceWith": { "$mergeObjects": [ { _id: "$"+station, first: "", last: "" }, "$station" ] } }
#     ])
#     query = db.testfile.aggregate(
#    [
#       {
#         "$project": {
#         station: 1,
#         station: { "$ifNull": [ "$"+station, "Unspecified" ] }
#         }
#       }
#    ]
# )
    for data in query:
        l.append(data[station])

    # db.testfile.updateMany(
    #     { URL: { $regex: /helloWorldt/ } },
    #     [{
    #         $set: { URL: {
    #         $replaceOne: { input: "$URL", find: "helloWorldt", replacement: "helloWorld" }
    #     }}
    # }]
    # )
    return l

def listStation():
    l = []
    data = db.test.find_one()
    for key in data:
        if(key not in ["month","year","day","date","_id"]):
            l.append(key)
    return l

def listDuplicate(columnName):
    test = db.test.aggregate([
    {"$group":{"_id":"$"+columnName,""+columnName:{"$first":"$"+columnName},"count":{"$sum":1}}},
    {"$match":{"count":{"$gt":1}}},
    {"$project":{""+columnName:1,"_id":0}},
    {"$group":{"_id":"",""+columnName:{"$push":"$"+columnName}}},
    {"$project":{"_id":0,""+columnName:1}}
    ])
    for i in test:
        result = i[columnName]
    return result

def getmonthrange():
    station = "300201"
    from_date = 2012
    to_date = 2013
    l = []
    for post in db.testfile.find({"year": {"$gte": from_date, "$lt": to_date}  } ,{station:1}):
        l.append(post[station])

    return l
# print(getmonth("432301","9","2013"))
print(getmonthrange())