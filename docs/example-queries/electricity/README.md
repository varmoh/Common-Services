# Electricity service API

## Fetch the lowest or highest electricity price for a specific date (default is today)
**Endpoints**
```
electricity/mock/lowest-price
electricity/lowest-price
electricity/mock/highest-price
electricity/highest-price
```

**Sample query - without date**
```
curl localhost:8080/electricity/mock/lowest-price
curl localhost:8080/electricity//lowest-price

curl localhost:8080/electricity/mock/highest-price
curl localhost:8080/electricity//highest-price
```

**Expected outcome**
```
{
    "response": [
        "2024-10-10",
        "23:00",
        0.0
    ]
}
```

**Sample query - with a specific date (userTime parameter)**
```
curl localhost:8080/electricity/mock/lowest-price?userTime=2024-05-05
curl localhost:8080/electricity/lowest-price?userTime=2024-05-05
```

**Expected outcome**
```
{
    "response": [
        "2024-05-05",
        "15:00",
        1.9
    ]
}
```
