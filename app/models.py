from flask_login import UserMixin
from app import db, mongo
from bson import ObjectId

# MongoDB User Wrapper for Flask-Login
class User(UserMixin):
    def __init__(self, user_doc):
        self.id = str(user_doc['_id'])  # Required by Flask-Login
        self.name = user_doc.get('name')
        self.email = user_doc.get('email')

# Required by Flask-Login
def load_user(user_id):
    try:
        user_doc = mongo.db.users.find_one({'_id': ObjectId(user_id)})
        if user_doc:
            return User(user_doc)
    except:
        return None
    return None

# SQLAlchemy Book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
