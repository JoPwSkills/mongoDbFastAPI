#import modules
from fastapi import FastAPI
from schema import MongoDBSchema
from config import collection
from bson import ObjectId

# create FastAPI instance
app = FastAPI()

# CREATE
@app.post('/mongodb_create')
def create_user(user: MongoDBSchema):
    dic = user.model_dump() #pydantic obj -> Dict
    response = collection.insert_one(dic)

    return {
        "id" : str(response.inserted_id)
    }

# READ ALL
@app.get('/mongodb_retrieve')
def retrieve_all():
    data = collection.find()
    return [
        {
            'id': str(i['_id']),
            'user_ud': i.get('user_id'),
            'bio': i.get('bio'),
            'interests': i.get('interests'),
            'social_link': i.get('social_link')

        }

        for i in data
    ]

# UPDATE
@app.put('/mongodb_update/{user_id}')
def update(user_id: str, bio: str):
    data = collection.find()
    collection.update_one(
        {'_id': ObjectId(user_id)},
        {"$set": {"bio": bio}}
    )

    return {'message': 'Update successfull'}


# DELETE 
@app.delete('/mongodb_delete/{user_id}')
def deleteUser(user_id:str):
    collection.delete_one(
        {
            '_id': ObjectId(user_id)
        }
    )

    return {'message': 'Delete Successfull'}