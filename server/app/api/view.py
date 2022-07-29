from .models import User
from app import db
from flask_restful import Resource, Api, fields, marshal_with, reqparse
from app.api import api_restfull_bp
from flask import jsonify, request, make_response
import datetime
import json
from app.utils import hundleResult

api = Api(api_restfull_bp)
resource_fields = {
    'id' : fields.Integer,
    'end_user_id' : fields.String,
    'web_page_url': fields.String,
}

subject_crud = reqparse.RequestParser()
subject_crud.add_argument('end_user_id', type=str, help='end_user_id is required!', required=True)
subject_crud.add_argument('web_page_url', type=str, help='web_page_url is required!', required=True)


class UserItem(Resource):

    def post(self):
        args = subject_crud.parse_args()
        print(args)
        try:
            user = User(end_user_id=args['end_user_id'], web_page_url=args['web_page_url'])
            db.session.add(user)
            db.session.commit()
            return make_response(jsonify({'id': user.id, 'end_user_id':user.end_user_id, 'web_page_url':user.web_page_url}))
        except:
            db.session.rollback()
            return make_response(jsonify({'id': user.id, 'end_user_id':user.end_user_id, 'web_page_url':user.web_page_url}))



#     @marshal_with(resource_fields, envelope='resource')
    def get(self, id=None):
        range = request.args.get('range', '[0,4]')
        range = range[1:-1].split(',')
        print(id)
        if id is None:
            user_all = User.query.all()[int(range[0]):int(range[1])+1]
            response = make_response(jsonify(hundleResult(user_all)))
            response.headers['X-Total-Count'] = '10'
            response.headers.add('Access-Control-Expose-Headers', 'Content-Range')
            response.headers.add('Content-Range', 'users : 0-9/'+str(User.query.count()))
            return response
        else:
            user = User.query.filter_by(id=id).first()
            response = make_response(jsonify({'id':user.id, 'end_user_id':user.end_user_id, 'web_page_url':user.web_page_url}))
            response.headers['X-Total-Count'] = '10'
            response.headers.add('Access-Control-Expose-Headers', 'Content-Range')
            response.headers.add('Content-Range', 'users : 0-9/'+str(User.query.count()))
#             if not user:
#                 return make_response(jsonify({'message': 'User not found!'}))
            return response

    # @marshal_with(resource_fields, envelope='resource')
    def delete(self, id):
        print(type(id))
        user = User.query.filter_by(id=id).first()
        if not user:
            return make_response(jsonify({'message': 'User not found!'}), 404)
        db.session.delete(user)
        db.session.commit()
        return  make_response(jsonify({'message': 'User has been deleted'}))

#     # @marshal_with(resource_fields, envelope='resource')
    def put(self, id):
        user = User.query.filter_by(id=id).first()
        if not user:
            return make_response(jsonify({'message': 'User not found!'}), 404)
        args = subject_crud.parse_args()

        user.end_user_id = args['end_user_id']
        user.web_page_url = args['web_page_url']
        try:
            db.session.commit()
            return make_response(jsonify({'id': user.id, 'end_user_id':user.end_user_id, 'web_page_url':user.web_page_url}))
        except:
            db.session.rollback()
            return make_response(jsonify({'id': user.id, 'end_user_id':user.end_user_id, 'web_page_url':user.web_page_url}))


api.add_resource(UserItem, '/users', '/users/<int:id>')