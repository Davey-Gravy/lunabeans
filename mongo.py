import pymongo

client = pymongo.MongoClient(
    "mongodb://root:password@localhost:27778/?directConnection=true"
)
collection = client['test']
print(collection)