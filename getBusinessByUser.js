use yelp

db.training.review.aggregate([
    {$match:{user_id:'nDBly08j5URmrHQ2JCbyiw'}},
    {$group:
        {
            _id:"$user_id",
            num_reviews:{$sum:1},
            business:{$push:{business_id:"$business_id",starts:"$stars"}}
        }
    },
    {$sort:{_id:1}}
    ])
