from flask import Flask, request
import uuid

app = Flask(__name__)
items =  {
         "719cd7fcaa6644698eab0ceec741d867":{
                                          "name": "Green mojhito",
                                           "price": 200
                                            },

        "d786fd9073a54cf9aa2574662b1c4623":{
                                           "name": "Momos",
                                            "price": 90
                                             }

}

@app.get('/get-items')
def get_items():
    return  {"items": items}

@app.get('/get-item/<string:name>')
def get_item(id):
   id = request.args.get['id']
   try:
    return items[id]
   except KeyError: 
        return {"message": " doesnot exits"}

@app.post('/add-item')
def add_item():
    request_data = request.get_json()
    items[uuid.uuid4().hex] = request_data
    return {"message": "item added succesfully"}


@app.put('/update-item')
def update_item():
    request_data = request.get_json()
    for item in items:
        if item['name'] == request_data['name']:
           item['price'] = request_data['price']
           return {"message": "item updated succesfully"}
    return {"message": "Given record doesnot exits"},404



@app.delete('/delete-item')
def delete_item():
    name = request.args.get('name')
    for item in items:
        if name == item['name']:
         items.remove(item)
         return {"message": "item deleted succesfully"}
    return {"message": "Given record doesnot exits"},404