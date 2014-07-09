System of Record
================

[![Build Status](https://travis-ci.org/LandRegistry/system-of-record.svg)](https://travis-ci.org/LandRegistry/system-of-record)

## Storage of minted title entries

Service to create new versions of a title, hashed and signed.

### Try it out

Check out the repo. Then cd into the repo directory:

 Create a virtualenv (assuming you have virtualenv and virtualenvwrapper installed)

 ```
 mkvirtualenv system-of-record
 ```

 **Install some stuff**

 Install dependencies into the virtualenv

```
pip install -r requirements
```

#### Create a local Postgres db.

Assuming you have postgres 9.3 installed and running

##### OSX

```
createuser -s sysofrec
```
 That should work out of the box if you're on OSX using Postgres.app.

Create the sysofrec database
```
createdb -U sysofrec -O sysofrec sysofrec -T template0
```

Export a couple of environment variables

For the moment export the following:

```
export SETTINGS='config.Config'
export  DATABASE_URL='postgresql://localhost/sysofrec'
```

For the future you can create a .env file alongside the Profile with this content

```
SETTINGS=config.Config
DATABASE_URL=postgresql://localhost/sysofrec
```

It's a special file that if sitting alongside a Procfile, foreman will use to create the environment variables contained. So anytime you run using
the run.sh (which uses foreman) these will be set.

###### psycopg on Mac

If ```pip install -r requirements.txt``` fail on Mac, try pointing your PATH to Postgres.App:


    export PATH=$PATH:/Applications/Postgres.app/Contents/Versions/9.3/bin

#####  Linux

The intial createuser may ask for a password and whether user should be super user. If so, add a password and and say yes to give
all privileges. This is only for local development so let's be relaxed. If you have created the user with a password change the last line of .env to this:

```
export export DATABASE_URL='postgresql://sysofrec:password@localhost/sysofrec'
```

#### Create the schema

There's an intial migration script in the project created using Flask-Migrate so you just need to call the following

```
python manage.py db upgrade

```

#### Run the app

```
./run.sh
```

**POST some data**

```
curl -X POST -H "Content-Type: application/json" -d '{"address": "1 low street", "title_number": "TN1234567",  "created_ts": 1210101 }' http://localhost:5002/titles/TN1234567
```


**GET some data**

```
curl -H "Accept: application/json"  http://localhost:5002/titles/TN1234567
```

Which should return:

```
{
  "title": {
    "data": "{u'title_number': u'TN1234567', u'created_ts': 1210101, u'address': u'1 low street'}",
    "number": "TN1234567"
  }
}
```

### Seeing everything in the store

```
curl -H "Accepts application/json"  http://localhost:5002/titles
```

 **Not implemented yet **

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

### Run the tests

```
 python -m unittest discover
```

**Note the only real tests are commented out for this pull request. Please uncomment and fix :)**


### TODO

Check incoming title entry for integrity using public key.
