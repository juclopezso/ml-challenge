import os
from werkzeug.utils import secure_filename
from app.main import db
from app.main.model.item import Item
from app.main.config import basedir


def get_items():
    return Item.query.all().limit(50)


def get_item(id):
    return Item.query.filter_by(id=id).first()


def bulk_save_items(data):
    # item = Item.query.filter_by(id=data['id']).first()
    # if item:
    #   response_object = {
    #       'status': 'fail',
    #       'message': 'Item already exists',
    #   }
      # return response_object, 409 # conflict

    #TODO: service logic here
    print("ITEM DATA:", data)

    file = data['file']

    if data['file']:
      filename = secure_filename(file.filename)
      # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      file.save(os.path.join(basedir, filename))
      print(file)


    # new_item = Item(*data)
    # save_changes(new_item)
    response_object = {
        'status': 'success',
        'message': 'Item successfully created.'
    }
    return response_object, 201 # created



def save_changes(data):
    db.session.add(data)
    db.session.commit()