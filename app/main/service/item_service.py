import os
import tempfile
from datetime import datetime
from werkzeug.utils import secure_filename
from app.main import db
from app.main.model.item import Item
from app.main.util.file_read import handle_file


def get_items():
    return Item.query.limit(50).all()


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

    if data['file'] is None or data['file'].filename == '':
        response_object = {
            'status': 'fail',
            'message': 'No file selected',
        }
        return response_object, 400

    file = data['file']
    # save the file temporarily 
    curr_datetime = datetime.utcnow().isoformat()
    filename = secure_filename(curr_datetime + '_' + file.filename)
    # filepath to temporary directory
    filepath = os.path.join(tempfile.gettempdir(), filename)
    file.save(filepath)
    init_time = datetime.now()

    try:
      db.session = db.create_scoped_session()
      # handle the file
      items = handle_file(filepath)
      # bulk save in db
      db.session.bulk_save_objects(items)
      db.session.commit()

    except Exception as err:
      print(err)
      response_object = {
          'status': 'fail',
          'message': 'Error saving items file',
      }
      return response_object, 500

    finally:
      # remove the file
      os.remove(filepath)

    end_time = datetime.now()
    # new_item = Item(*data)
    # save_changes(new_item)
    response_object = {
        'status': 'success',
        'message': f'Items successfully created in {(end_time - init_time)}.'
    }
    return response_object, 201 # created


def save_changes(data):
    db.session.add(data)
    db.session.commit()