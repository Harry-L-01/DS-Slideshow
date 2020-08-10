from .extensions import db, login_manager
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String())

    def __repr__(self):
        return f'{self.id}, {self.username}'

class Content(db.Model):
    path = db.Column(db.String(), primary_key=True)
    priority = db.Column(db.Integer, unique=True)
    type = db.Column(db.String(4))  # img, link, vid

    def __repr__(self):
        return f'{self.path}, {self.priority}'

@login_manager.user_loader
def load_user(user_id : str) -> User:
    # should always return 1 until other users are supported
    return User.query.get(int(user_id))