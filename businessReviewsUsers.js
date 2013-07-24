use yelp

db.training.review.aggregate([
    {$group:
        {
            _id:"$business_id",
            num_reviews:{$sum:1},
            avg_starts:{$avg:"$stars"},
            users:{$push:{user:"$user_id",starts:"$stars"}}
        }
    },
    {$sort:{_id:1}}
    ])
