import os
import tempfile
import asyncio
from datetime import datetime
from werkzeug.utils import secure_filename
from app.main import db
from app.main.model.item import Item
# from app.main.util.file_read import handle_file
# from app.main.util.file_read_async import handle_file
from app.main.util.file_read_async_optimized import handle_file


def get_items():
    return Item.query.limit(100).all()


def get_item(id):
    return Item.query.filter_by(id=id).first()


def bulk_save_items(data):
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
      asyncio.run(create_items_from_file(filepath))

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
    response_object = {
        'status': 'success',
        'message': f'Items successfully created in {(end_time - init_time)}.'
    }
    return response_object, 201 # created


async def create_items_from_file(filepath):
    db.session = db.create_scoped_session()
    # handle the file
    items = await handle_file(filepath)
    print("Inserted Items:", len(items))
    # bulk save in db
    db.session.bulk_save_objects(items)
    db.session.commit()

