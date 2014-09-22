object_id_1 = "AB1234567"
object_id_2 = "BC123454"

data_from_mint = {
        "public_key": "this would be a key",
        "title_number": object_id_1,
        "sha256": "a hash of the title below",
        "title": {
            "title_number":  object_id_1,
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
            "titles": [object_id_1]
        }
    }
}

data_from_mint_2 = {
    "public_key": "this would be a key",
    "title_number": object_id_2,
    "sha256": "a hash of the title below",
    "title": {
        "title_number":  object_id_1,
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
            "titles": [object_id_1]
        }
    }
}
