from flask import request, make_response, jsonify
import json
from flask import current_app as app
from .api.models import User
from app import db, socketio
from .utils import hundleResult
from flask_socketio import send, emit
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
        users = User.query.all()
        socketio.send(hundleResult(users))
        return {'success':True}
    except:
        db.session.rollback()
        return {'success':False}


@socketio.on('connect')
def test_connect(auth):
   users = User.query.all()
   socketio.send(hundleResult(users))
   print('Client connected')

# @socketio.on('remote-call')
# def remote_call():
# #    a, b = data
#    print('emmittt')
#    users = User.query.all()
#    socketio.emit('get-data', hundleResult(users))
# #    callback(users)
# #    socketio.send(hundleResult(users))


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')
