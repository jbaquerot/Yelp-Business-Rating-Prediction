use yelp

db.training.userCategories.aggregate([
    {$match:{categories:{$all: ["Ice Cream & Frozen Yogurt",
                           "Food",
                           "Japanese",
                           "Creperies",
                           "Sushi Bars",
                           "Restaurants"]}}
    },
    {$unwind : "$categories"},
    {$group:
        {
            _id:"$user_id",
            num_cat:{$sum:1}
        }
    },
    {$sort:{num_cat:1}},
    {$limit:1}
])
