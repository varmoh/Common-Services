# Electrc service API - lowest electricity price

## Displays the lowest electricity price
**Endpoints**
```
electricity/mock/lowest-price
electricity/lowest-price
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

## Displays the lowest electricity price for the chosen day 
**Endpoints**
```
electricity/mock/lowest-price?userTime=2024-05-05
electricity/lowest-price?userTime=2024-05-05
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
