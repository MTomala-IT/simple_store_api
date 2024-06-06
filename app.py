from flask import Flask, request

# create flask  app, able to run the app, flask looks inside the folder for var called app
app = Flask(__name__)

# define DB,  temporarily it will be a local DB
stores = [
    {
        "name": "my_store",
        "items": [
            {
                "name": "chair",
                "price": 15.99
            }
        ]
    }
]


# create the endpoint and the function what returns the data, flask route, endpoint definition
@app.get("/store")  # http://127.0.0.1:5000/store
def get_stores():
    return {"stores": stores}


# endpoint for creating the stores with their names
@app.post("/store")
def create_store():
    # request turns data into a dict
    request_data = request.get_json()
    new_store = {
        "name": request_data["name"],
        "items": []
    }
    stores.append(new_store)
    return new_store, 201


# create dynamic endpoint, query string parameter: /store?name=My Store/item
@app.post("/store/<string:name>/item")
def create_item(name):
    # grab the incoming json
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {
                "name": request_data["name"],
                "price": request_data["price"]
            }
            # append items for the store we are in currently
            store["items"].append(new_item)
            return new_item, 201
    # this return wil never be  reached if  the store exists
    return {"message": "Store not found"}, 404


@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store
    # this return wil never be reached if the store exists
    return {"message": "Store not found"}, 404


# get the specific item from the store
@app.get("/store/<string:name>/item")
def get_item_in_store(name):
    for store in stores:
        if store["name"] == name:
            # return dict, not a list, ease of mod it in the future, like adding tags etc
            return {"items": store["items"]}
    # this return wil never be  reached if  the store exists
    return {"message": "Store not found"}, 404
