from flask import request
from flask_restx import Resource
from ..util.dto import ItemCreatetDto, ItemDto
from ..service.item_service import get_items, get_item, bulk_save_items

api = ItemDto.api
_item = ItemDto.item
_item_create = ItemCreatetDto.parser


# decorator for route resources
@api.route('/')
class ItemList(Resource):
    @api.doc('list_of_items')
    @api.marshal_list_with(_item, envelope='data')
    def get(self):
        return get_items()

    @api.doc('bulk_save_items')
    @api.expect(_item_create)
    def post(self):
        req_args = _item_create.parse_args()
        return bulk_save_items(req_args)


@api.route('/<id>')
@api.param('id', 'The item identifier')
@api.response(404, 'Item not found.')
class Item(Resource):
    @api.doc('get an item')
    @api.marshal_with(_item)
    def get(self, id):
        item = get_item(id)
        if not item:
            api.abort(404)
        else:
            return item
