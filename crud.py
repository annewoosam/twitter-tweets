"""CRUD operations."""

from model import db, Tweet, connect_to_db

import datetime


def create_tweet(handle, post_or_reply, url, content, comments, views, hearts, last_updated):
   

    tweet = Tweet(handle=handle,
                  post_or_reply=post_or_reply,
                  url=url,
                  content=content,
                  comments=comments,
                  comment_summary=comment_summary,
                  views=views,
                  hearts=hearts,
                  last_updated=last_updated)

    db.session.add(tweet)

    db.session.commit()

    return tweet

def get_tweets():
    """Return all rows of tweet data."""

    return Tweet.query.all()

def create_comment(commentator, comment_summary, replied_to, last_updated):

    comment=Comment(commentator=commentator,
                    comment_summary=comment_summary,
                    replied_to=replied_to,
                    last_updated=last_updated)   

    db.session.add(comment)

    db.session.commit()

    return comment
 
if __name__ == '__main__':
    from server import app
    connect_to_db(app)
