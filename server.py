"""Server for YourFolder app."""

# increased flask

from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# created import allowing connection to database

from model import connect_to_db, Tweet, Comment db

app = Flask(__name__)

# imported Jinja secret key settings
from jinja2 import StrictUndefined

app.secret_key = "dev"

app.jinja_env.undefined = StrictUndefined

import crud

@app.route('/')

def all_tweetsandcomments():

    stats=crud.get_tweets()
    
    tweet_post_id=[q[0] for q in db.session.query(Tweet.twitter_post_id).all()]

    handle=[q[0] for q in db.session.query(Tweet.handle).all()]
      
    post_or_reply=[q[0] for q in db.session.query(Tweet.post_or_reply).all()]
    
    url=[q[0] for q in db.session.query(Tweet.url).all()]

    content=[q[0] for q in db.session.query(Tweet.content).all()]

    comments=[q[0] for q in db.session.query(Tweet.comments).all()]

    views=[q[0] for q in db.session.query(Tweet.views).all()]

    hearts=[q[0] for q in db.session.query(Tweet.hearts).all()]

    comment_id=[q[0] for q in db.session.query(Comment.comment_id).all()]

    commentator=[q[0] for q in db.session.query(Comment.commentator).all()]

    comment_summary=[q[0] for q in db.session.query(Comment.comment_summary).all()]

    replied_to=[q[0] for q in db.session.query(Comment.replied_to).all()]

    last_updated=[q[0] for q in db.session.query(Comment.last_updated).all()]

    return render_template('tweetsandcomments.html', tweet_post_id=tweet_post_id, handle=handle, post_or_reply=post_or_reply, url=url, content=content, comments=comments, views=views, hearts=hearts, commentator=commentator, comment_summary=comment_summary, replied_to=replied_to, last_updated=last_updated)

if __name__ == '__main__':

# added connection to database

    connect_to_db(app)

# during development

    app.run(host='0.0.0.0', debug=True)

# in production

    #app.run()