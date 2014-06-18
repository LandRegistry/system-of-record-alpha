
## S3 backed storage of minted title entries

Service to create new versions of a title, hashed and signed.

### Try it out

Create an S3 bucket

**Set some environment variables**

 ```
export AWS_KEY=YOUR_KEY
export S3_BUCKET='some-bucket-name'
export AWS_SECRET=YOUR_AWS_SECRET
```

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
curl -X POST -H "Content-Type: application/json" -d '{"address": "1 low street", "title_number": "TN1234567", "sha256":  "a27e6eda1e0c12161e28d88332c158ea4b49dcf333b5b2278569cace13c2d428"}' http://localhost:5000/titles
```

That should write two entries to the S3 bucket with the keys ```TN1234567/head.json``` and another file with same content named ```a27e6eda1e0c12161e28d88332c158ea4b49dcf333b5b2278569cace13c2d428.json```


** What you will see on S3**

![Document on S3](http://i.imgur.com/D4VzxpA.png)

Subsequent writes for the same title number will  also write the file contents with sha256 sum as name and over write the head.json so that head.json will be the latest,
current title entry.


**GET some data**

```
curl -H "Accepts: application/json"  http://localhost:5000/titles/TN1234567
```

Which should return:

```
{
  "address": "1 low street",
  "sha256": "a27e6eda1e0c12161e28d88332c158ea4b49dcf333b5b2278569cace13c2d428",
  "title_number": "TN1234567"
}
```


### Stuff I'm adding/changing v soon.

Add in memory store so that local testing easy (i.e. no s3 bucket needed)
Check incoming title entry for integrity
