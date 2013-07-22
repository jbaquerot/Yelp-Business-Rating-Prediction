use yelp

db.training.business.aggregate([
    {$unwind:"$categories"},
    {$group:
        {
            _id:"$categories",
            num_business:{$sum: 1}
        }
    },
    {$sort:{num_business:1}}
    ])
