use yelp

db.training.review.aggregate([
    {$group:
        {
            _id:"$user_id",
            num_reviews:{$sum:1},
            business:{$push:"$business_id"},
            starts:{$push:"$stars"}
        }
    },
    {$sort:{_id:1}}
    ])
