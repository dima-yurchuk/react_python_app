from app import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    end_user_id = db.Column(db.String(25), nullable=False)
    web_page_url = db.Column(db.String(200), nullable=False)


    def __repr__(self):
        return f'<Task {self.id} {self.end_user_id} {self.web_page_url}>'