title_id = "AB1234567"
title_id_2 = "BC123454"

data_from_mint = {
        "public_key": "this would be a key",
        "title_number": title_id,
        "sha256": "a hash of the title below",
        "title": {
            "title_number":  title_id,
            "proprietors": [
            {
                "first_name": "Vile",
                "last_name": "Bawd"
            }
        ],
        "property":{
            "address": {
                "house_number": "1",
                "road": "Muddy Land",
                "town": "The Hovel",
                "postcode": "ABC 123"
            },
            "tenure": "freehold",
            "class_of_title": "absolute"
        },

        "payment": {
            "price_paid": "3",
            "titles": [title_id]
        }
    }
}

data_from_mint_2 = {
    "public_key": "this would be a key",
    "title_number": title_id_2,
    "sha256": "a hash of the title below",
    "title": {
        "title_number":  title_id,
        "proprietors": [
            {
                "first_name": "Vile",
                "last_name": "Bawd"
            }
        ],
        "property":{
            "address": {
                "house_number": "1",
                "road": "Muddy Land",
                "town": "The Hovel",
                "postcode": "ABC 123"
            },
            "tenure": "freehold",
            "class_of_title": "absolute"
        },

        "payment": {
            "price_paid": "3",
            "titles": [title_id]
        }
    }
}