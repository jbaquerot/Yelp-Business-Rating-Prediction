import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt

#Reading Files
#Business
fileBusiness = './yelp_training_set/yelp_training_set_business.json'
business_tmp = pd.DataFrame([json.loads(line) for line in open(fileBusiness)])
business_tmp.rename(columns={'categories':'business_categories','city':'business_city','full_address':'business_full_address',
                         'latitude':'business_latitude','longitude':'business_longitude','name':'business_name',
                         'neighborhoods':'business_neighborhoods','open':'business_open',
                         'review_count':'business_review','stars':'business_stars','state':'business_state',
                         'type':'business_type'}, inplace=True)
#adding categories columns
categories_iter = (set(x) for x in business_tmp.business_categories)

categories = sorted(set.union(*categories_iter))

dummies = pd.DataFrame(np.zeros((len(business_tmp),len(categories))), columns=categories)

for i,cat in enumerate(business_tmp.business_categories):
    for c in cat:
        dummies.ix[i,c] = 1

business = business_tmp.join(dummies.add_prefix('category_'))
del business_tmp
del dummies

#Checkings

fileCheckings = './yelp_training_set/yelp_training_set_checkin.json'
checkins_tmp = pd.DataFrame([json.loads(line) for line in open(fileCheckings)])
checkins_tmp.rename(columns={'type':'checkin_type'}, inplace=True)

#Adding checkinfo columns
checkinfo_iter = (set(x) for x in checkins_tmp.checkin_info)

categories = sorted(set.union(*checkinfo_iter))

dummies = pd.DataFrame(np.empty((len(checkins_tmp),len(categories)), dtype=str), columns=categories)

for i,cat in enumerate(checkins_tmp.checkin_info):
    for c,val in cat.items():
        dummies.ix[i,c] = val
        

checkins = checkins_tmp.join(dummies.add_prefix('info_'))

del checkins_tmp
del dummies




#Reviews
fileReviews =  './yelp_training_set/yelp_training_set_review.json'
reviews_tmp = pd.DataFrame([json.loads(line) for line in open(fileReviews)])
reviews_tmp.rename(columns={'date':'review_date','stars':'review_stars','text':'review_text','type':'review_type',
                        'votes':'review_votes'}, inplace=True)
#Adding votes colums

review_iter = (set(x) for x in reviews_tmp.review_votes)

categories = sorted(set.union(*review_iter))

dummies = pd.DataFrame(np.empty((len(reviews_tmp),len(categories)), dtype=str), columns=categories)

for i,cat in enumerate(reviews_tmp.review_votes):
    for c,val in cat.items():
        dummies.ix[i,c] = val
        

reviews = reviews_tmp.join(dummies.add_prefix('votes_'))

del dummies
del review_iter


#Users
fileUsers = './yelp_training_set/yelp_training_set_user.json'
users_tmp = pd.DataFrame([json.loads(line) for line in open(fileUsers)])
users_tmp.rename(columns={'name':'user_name', 'type':'user_type', 'average_stars':'user_average_stars','votes':'user_votes',
                      'review_count':'user_review_count'}, inplace=True)
#Adding votes colums

user_iter = (set(x) for x in users_tmp.user_votes)

categories = sorted(set.union(*user_iter))

dummies = pd.DataFrame(np.empty((len(users_tmp),len(categories)), dtype=str), columns=categories)

for i,cat in enumerate(users_tmp.user_votes):
    for c,val in cat.items():
        dummies.ix[i,c] = val
        

users = users_tmp.join(dummies.add_prefix('votes_'))

del users_tmp
del dummies



#dataSet = pd.merge(pd.merge(pd.merge(reviews,users, on='user_id',how='outer'), business, on='business_id',how='outer'), checkins, on='business_id',how='outer')
