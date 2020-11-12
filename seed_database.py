"""Script to seed database."""

import os

import json

from datetime import datetime

import crud

import model

import server


os.system('dropdb twitter_tweets')

os.system('createdb twitter_tweets')

model.connect_to_db(server.app)

model.db.create_all()


# Create tweets table's initial data.

with open('data/tweet.json') as f:

    tweet_data = json.loads(f.read())

tweet_in_db = []

for tweet in tweet_data:
    handle, post_or_reply, url, content, comments, views, hearts, last_updated = (
                                   tweet['handle'],
                                   tweet['post_or_reply'],
                                   tweet['url'],
                                   tweet['content'],
                                   tweet['comments'],
                                   tweet['views'],
                                   tweet['hearts'],
                                   tweet['last_updated'])

    db_tweet = crud.create_tweet(
                                 handle,
                                 post_or_reply,
                                 url,
                                 content,
                                 comments,
                                 views,
                                 hearts,
                                 last_updated)

    tweet_in_db.append(db_tweet)

# Create comments table's initial data.

with open('data/comment.json') as f:

    comment_data = json.loads(f.read())

comment_in_db = []

for comment in comment_data:
    commentator, comment_summary, replied_to, last_updated = (
                                   comment['commentator'],
                                   comment['comment_summary'],
                                   comment['replied_to'],
                                   comment['last_updated'])

    db_comment = crud.create_comment(
                                 commentator,
                                 comment_summary,
                                 replied_to,
                                 last_updated)

    comment_in_db.append(db_comment)