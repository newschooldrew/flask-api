from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []


class Item(Resource):

    def get(self, name):
        item = next(filter(lambda item: item['name'] == item, items), None)
        # next gives us the first item in this filter function

        # for item in items:
        #     if item['name'] == name:
        #         return item
        return {'item': item}, 200 if item else 404

    def post(self, name):
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201


class ItemList(Resource):
    def get(self):
        return {'items': items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000)
