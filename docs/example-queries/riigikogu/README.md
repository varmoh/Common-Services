# Riigikogu Services API Documentation

## Get member participation statistics

**Endpoint**
```
iigikogu/mock/member-participation
riigikogu/member-participation
```

**Accepts parameters**
```
starDate    # not required, defaults to endDate - 30 days 
endDate     # not required, defaults to Today
memberName  # required, otherwise query fails
```

**Sample Query**
```
curl "localhost:8080/services/member-participation?memberName=Jüri%20Ratas&startDate=2024-09-01&endDate=2024-09-30"
```

**Expected outcome**
```
# If the member "Jüri Ratas" exists in the system and has participation data within the specified date range

{
    "response": "Jüri Ratas on olnud perioodil 2024-09-01 - 2024-09-30 kohal 20 korda ja puudunud 5 korda."
}
```

## Get the latest voting results from Riigikogu

**Endpoint**
```
riigikogu/recent-voting
riigikogu/mock/recent-voting
```

**Sample Query**
```
curl "localhost:8080/riigikogu/recent-voting"
```

**Expected outcome**
```
# If the latest voting data is successfully retrieved

{
    "response": "'Eelnõu X', Poolt on 50, Vastu on 30, Neutraalsed 10, Ei hääletanud 5"
}
```

## Fetch 5 Most Recent Voting Results

**Endpoint**
```
riigikogu/five-most-recent
riigikogu/mock/five-most-recent
```

**Sample Query**
```
curl "localhost:8080/services/most-recent-votings"
```

**Expected outcome**
```
{
    "response": [
        {
            "title": "Perehüvitiste seaduse muutmise seadus",
            "present": 81,
            "absent": 20,
            "inFavor": 46,
            "against": 20,
            "neutral": 0,
            "abstained": 15
        },
        {
            "title": "Vabariigi Valitsuse seaduse muutmise seadus",
            "present": 84,
            "absent": 17,
            "inFavor": 53,
            "against": 25,
            "neutral": 0,
            "abstained": 6
        }
        ...
    ]
}

```