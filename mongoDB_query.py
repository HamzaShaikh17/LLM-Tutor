import pymongo

from datetime import date
today = date.today()

def db_update(user_id,question,answer):
    user_id = "38001"
    client = (pymongo.MongoClient("mongodb://localhost:27017"))
    print(client)
    db = client['LLM_Tutor']
    collection = db[user_id]

    date2 = today.strftime('%B %d, %Y')
    print('date2 =', date2)

    dictionary = {"time":str(date2),"question": question,"answer":answer}
    collection.insert_one(dictionary)
    print("query updated")