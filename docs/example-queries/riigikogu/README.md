# Member Participation Statistics Service Documentation

## Get member participation statistics for Riigikogu

**Endpoint**
```
localhost:8080/riigikogu/mock/member-participation
localhost:8080/riigikogu/member-participation
```

**Accepts parameters**
```
starDate    # not required, defaults to endDate - 30 days 
endDate     # not required, defaults to Today
memberName  # required, otherwise query fails
```

**Description**
This service provides participation statistics for Riigikogu members. It allows you to specify a date range and fetches the attendance and absence data for a given member.

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
/services/votings/latest
/services/votings/latest
```

**Description**
This service retrieves the most recent voting results from Riigikogu. It provides the title of the voting along with details about how many members voted in favor, against, were neutral, or abstained.

**Sample Query**
```
curl "localhost:8080/services/votings/latest"
```

**Expected outcome**
```
# If the latest voting data is successfully retrieved

{
    "response": "'Eelnõu X', Poolt on 50, Vastu on 30, Neutraalsed 10, Ei hääletanud 5"
}