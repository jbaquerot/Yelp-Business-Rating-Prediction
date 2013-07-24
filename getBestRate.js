use yelp

db.training.review.aggregate([
    {$match:
        {
            user_id: {$in: ['q9XgOylNsSbqZqF_SO3-OQ', 'l53FUDHRHLg7BQ89KgAtxQ', 'usQTOj7LQ9v0Fl98gRa3Iw', 'fczQCSmaWF78toLEmb0Zsw']},
            business_id: {$in : ['QL3vFMAsEHqfi1KGH-4igg', 'WNy1uzcmm_UHmTyR--o5IA', '2qbajPD8M7PJlWWaHSRR5Q', 'xKXahNKbBUZtOPWibwq94w']}
        }
    },
    {$group:
        {
            _id: null,
            avg_stars:{$avg:"$stars"},
            max_stars:{$max:"$stars"},
            min_stars:{$min:"$stars"}
        }
    }
])
