from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

clinent = MongoClient(uri)

db = clinent.get_default_database()

posts = db["posts"]

post = {
    "title": "I cant live without code",
    "author": "By Linh Hoang C4E22",
    "content": "if you participate on this community, you can realize who you are and see your future "
}

posts.insert_one(post)

print(post)