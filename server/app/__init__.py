from flask import Flask
from flask_sock import Sock
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO


db = SQLAlchemy()
# sock = Sock()
socketio = SocketIO()
def create_app(config_filename=None):
    app = Flask(__name__)
    with app.app_context():
        app.config['SECRET_KEY'] = 'asfdsfsaaf'
        app.config['WTF_CRSF_ENAVLED'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        CORS(app, resources={r"/*":{"origins":"*"}})
        db.init_app(app)
#         sock.init_app(app)
        socketio.init_app(app, cors_allowed_origins="*")
        from .api import api_restfull_bp
        app.register_blueprint(api_restfull_bp, url_prefix='/api')
        from app import view
    return app
app = create_app()


