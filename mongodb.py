# from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient


# load_dotenv(find_dotenv())
pwd = 'Gowtham12345%40'
connection_string = f"mongodb+srv://gowtham:{pwd}@netflix-clone.9thyurk.mongodb.net/?retryWrites=true&w=majority"
# connection_string = "mongodb://localhost:27017"

client = MongoClient(connection_string)

# dbs = client.list_database_names()
bmi_us = client["registration_pbi"]
# collections = bmi_us.list_collection_names()


def insert(name, ph_no, mail_id):
    collection = bmi_us["test"]
    doc = {"name": name,
           "email": mail_id, "ph_no": ph_no}
    inserted_id = collection.insert_one(doc).inserted_id
    print(inserted_id)
    return doc


def find(mail_id):
    collection = bmi_us["test"]
    doc = collection.find_one({"email": mail_id})
    # pprint.pprint(doc)
    return doc

