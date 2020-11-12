from flask_sqlalchemy import SQLAlchemy

import datetime

db = SQLAlchemy()

class Tweet(db.Model):
    """A class for tweets ."""
    
    __tablename__ = 'tweets'

    twitter_post_id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    handle = db.Column(db.String)

    post_or_reply = db.Column(db.String)

    url = db.Column(db.String)

    content = db.column(db.String)

    comments = db.column(db.Integer)

    views = db.Column(db.Integer)

    hearts = db.Column(db.Integer)

    last_updated = db.Column(db.Date)

    def __repr__(self):
        return f'<Tweet twitter_post_id={self.twitter_post_id} handle={self.handle}>'

class Comment(db.Model):
    """A class for comments."""
    
    __tablename__ = 'comments'

    comment_id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    commentator = db.Column(db.String)

    comment_summary = db.Column(db.String)

    replied_to = db.Column(db.String)

    last_updated=db.Column(db.Date)

    def __repr__(self):
        return f'<Tweet twitter_post_id={self.twitter_post_id} handle={self.handle}>'

def connect_to_db(flask_app, db_uri='postgresql:///twitter-tweets', echo=True):
   
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
   
    flask_app.config['SQLALCHEMY_ECHO'] = echo
   
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    
    db.init_app(flask_app)

    print('Connected to the db!')

if __name__ == '__main__':

    from server import app

    connect_to_db(app)