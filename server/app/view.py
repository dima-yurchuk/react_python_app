from flask import request, make_response, jsonify
import json
from flask import current_app as app
from .api.models import User
from app import db
from .utils import hundleResult

user_data = []


@app.route('/user/save', methods=['GET', 'POST'])
def save_user():
    data = request.get_json()
    data['id']='123'
    user_data.append(data)
    user = User(end_user_id=data['end_user_id'], web_page_url=data['web_page_url'])
    try:
        db.session.add(user)
        db.session.commit()
        return {'success':False}
    except:
        db.session.rollback()
        return {'success':False}
