import pymongo # pip install pymongo
import pandas as pd
import json

client = pymongo.MongoClient("mongodb+srv://rakesh:rakesh3210@cluster0.ytkfwzz.mongodb.net/?retryWrites=true&w=majority")

DATA_FILE_PATH = (r"notebooks/Visadataset.csv")
DATABASE_NAME = "US_VISA"
COLLECTION_NAME = "visa_data"


if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")

    df.reset_index(drop = True, inplace = True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)