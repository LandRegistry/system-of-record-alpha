System of Record
================

[![Build Status](https://travis-ci.org/LandRegistry/system-of-record.svg)](https://travis-ci.org/LandRegistry/system-of-record)

## Storage of minted title entries

Service to create new versions of a title, hashed and signed.

### Try it out

Note that you can run using an in memory/temporary store of records if you skip the S3 part below.

 **Install some stuff**

```
pip install -r requirements
```

**Run locally outside of a container**

```
 ./manage.py runserver
```

**POST some data**

```
curl -X POST -H "Content-Type: application/json" -d '{"address": "1 low street", "title_number": "TN1234567",  "created_ts": 1210101 }' http://localhost:8001/last```
```


**GET some data**

```
curl -H "Accept: application/json"  http://localhost:5000/last
```

Which should return:
```
TN1234567: {
    address: "1 low street",
    created_ts: 1210101,
    sha256: "e27e7eda1e0c12161e28d89532c158ea4b49dcf333b5b2278569cace13c2d428",
    title_number: "TN1234567"
}
```

### Seeing everything in the store

```
curl -H "Accepts application/json"  http://localhost:5000/titles
```

Returns something like this for now.

```
{
titles: [
    {
        TN1234567: {
            address: "1 low street",
            created_ts: 1010101010,
            sha256: "a27e6eda1e0c12161e28d88332c158ea4b49dcf333b5b2278569cace13c2d428",
            title_number: "TN1234567"
            }
        },
        {
        TN9876543: {
            address: "1 middle street",
            created_ts: 1010101010,
            sha256: "a27e6eda1e0c12161e28d88332c158ea4b49dcf333b5b2278569cace13c2d428",
            title_number: "TN9876543"
            }
        },
        {
        TN9876578787878: {
                address: "1 high street",
                created_ts: 1010101010,
                sha256: "a27e6eda1e0c12161e28d88332c158ea4b49dcf333b5b2278569cace13c2d428",
                title_number: "TN9876578787878"
            }
        }
    ]
}
```


### TODO

Check incoming title entry for integrity using public key.
