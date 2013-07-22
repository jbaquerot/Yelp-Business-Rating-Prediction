import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt

#Reading Files
#Business
fileBusiness = './yelp_test_set/yelp_test_set_business.json'
business_test = pd.DataFrame([json.loads(line) for line in open(fileBusiness)])
business_test.rename(columns={'categories':'business_categories','city':'business_city','full_address':'business_full_address',
                         'latitude':'business_latitude','longitude':'business_longitude','name':'business_name',
                         'neighborhoods':'business_neighborhoods','open':'business_open',
                         'review_count':'business_review','stars':'business_stars','state':'business_state',
                         'type':'business_type'}, inplace=True)
#adding categories columns
categories_iter = (set(x) for x in business_test.business_categories)

categories = sorted(set.union(*categories_iter))

dummies = np.zeros((len(business_test),len(categories)))

for i,cat in enumerate(business_test.business_categories):
    for c in cat:
        dummies[i,categories.index(c)] =+ 1

dummies_array = [p for p in dummies]
business_test['business_cat']=pd.Series(dummies_array, dtype=np.dtype("object"))

#Checkings

#fileCheckings = './yelp_test_set/yelp_test_set_checkin.json'
#checkins_test = pd.DataFrame([json.loads(line) for line in open(fileCheckings)])


#Reviews
fileReviews =  './yelp_test_set/yelp_test_set_review.json'
reviews_test = pd.DataFrame([json.loads(line) for line in open(fileReviews)])


#reviews_test = pd.merge(business_test,reviews_tmp, on='business_id')
#userCategories_test = reviews_test['business_cat'].groupby(reviews_test['user_id']).agg({"business_cat": lambda x: list(x.sum())})
#userCategories_test['user_id']= userCategories_test.index


#Users
#fileUsers = './yelp_test_set/yelp_test_set_user.json'
#users_test = pd.DataFrame([json.loads(line) for line in open(fileUsers)])

#Read Trainig Data
#userCategories_training=pd.read_csv('userCategories.csv')
#userCategories_training['business_cat']=[eval(x) for x in userCategories_training['business_cat']]


#Solution

#reviews_test['stars'] = pd.Series(np.random.random(len(reviews_test)), index=reviews_test.index)

def findSimilarUser(userId, userCat, userCatTraining):
    minDist=1000000
    bestUser=''
    userCategories_test_sample= userCatTraining.take(np.random.permutation(len(userCategories_test))[:10])
    for u,c in userCategories_test_sample.itertuples(index=False):
        dist = np.sqrt(sum((a-b)**2 for a,b in zip(userCat, c)))
        if dist < minDist:
            minDist = dist
            bestUser = u
    return bestUser

#similarUsers=[findSimilarUser(u,c, userCategories_training) for c,u in userCategories_test.itertuples(index=False)]
#userCategories_test['similarUser'] = similarUsers

#userCategories_test.to_csv('userCategories_testi.csv')
userCategories_test=pd.read_csv('userCategories_test.csv')


#Users
fileUsers = './yelp_training_set/yelp_training_set_user.json'
users_tmp = pd.DataFrame([json.loads(line) for line in open(fileUsers)])
users_tmp.rename(columns={'name':'user_name', 'type':'user_type', 'average_stars':'user_average_stars','votes':'user_votes',
                      'review_count':'user_review_count'}, inplace=True)

users=users_tmp.merge(userCategories_test, left_on='user_id', right_on='similarUser')
solution = reviews_test.merge(users, how='outer', left_on='user_id', right_on='user_id.1')
solution.ix[np.isnan(solution['user_average_stars']),'user_average_stars']=0
del solution['type']
solution.to_csv('solution.csv', cols=['business_id','user_id','user_average_stars'],index=False)


