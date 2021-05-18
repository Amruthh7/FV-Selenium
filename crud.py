from pymongo import MongoClient
from bson.objectid import ObjectId
client=MongoClient('localhost',27017)
db=client.get_database("FV_assesment")
collection = db.get_collection("assesment")
print(db.list_collection_names())
print(client.list_database_names())
documents =[
{"Name":"Amruth","Gmail":"Abc","Phone Num":"1234"},
{"Name":"A","Gmail":"BCA","Phone Num":"1234"},
{"Name":"AB","Gmail":"AAA","Phone Num":"14"},
{"Name":"AAA","Gmail":"bb","Phone Num":"12"},
{"Name":"Amr","Gmail":"ahhcd","Phone Num":"1464"},
{"Name":"Amh","Gmail":"Asvsd","Phone Num":"1236464"},
{"Name":"Accs","Gmail":"Bssd","Phone Num":"12565"},
{"Name":"ABdd","Gmail":"scA","Phone Num":"15464"},
{"Name":"AcsAA","Gmail":"bcsb","Phone Num":"15462"},
{"Name":"Amr","Gmail":"ahhcd","Phone Num":"1464"}]
response=collection.insert_many(documents)
print(collection.find())
id=ObjectId("60a342d0261e5cab99983b03")
print(id)

lastid=response.inserted_ids
print("Last inserted id :",format(lastid))
