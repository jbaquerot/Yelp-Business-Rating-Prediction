#!/bin/bash


mongoimport --drop --db yelp --collection training.review --file ./yelp_training_set/yelp_training_set_review.json
mongoimport --drop --db yelp --collection training.user --file ./yelp_training_set/yelp_training_set_user.json 
mongoimport --drop --db yelp --collection training.checkin --file ./yelp_training_set/yelp_training_set_checkin.json 
mongoimport --drop --db yelp --collection training.business --file ./yelp_training_set/yelp_training_set_business.json





mongoimport --drop --db yelp --collection test.review --file ./yelp_test_set/yelp_test_set_review.json
mongoimport --drop --db yelp --collection test.user --file ./yelp_test_set/yelp_test_set_user.json 
mongoimport --drop --db yelp --collection test.checkin --file ./yelp_test_set/yelp_test_set_checkin.json 
mongoimport --drop --db yelp --collection test.business --file ./yelp_test_set/yelp_test_set_business.json

mongoimport --db yelp --collection training.business --file ./yelp_test_set/yelp_test_set_business.json 
mongoimport --db yelp --collection training.user --file ./yelp_test_set/yelp_test_set_user.json 

