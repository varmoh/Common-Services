# Statistics-Estonia service

***This service provides Consumer Price Index (CPI) change, Estimated Subsistence Minimum, and Unemployment Rate***

# API endpoints (GET)
```
/statistics-estonia/estimated-subsistence-minimum
/statistics-estonia/unemployment-rate
/statistics-estonia/consumer-price-index
```
##  * estimated-subsistence-minimum:
### Example passed parameters
```
  "chatId": "12345",
  "authorId": "user123"
```
### Example response
```
[
  {
    "chatId": "12345",
    "content": "Arvestuslik elatusmiinimum on 338.23€/ kuus",
    "buttons": [
      {
        "title": "More Info",
        "payload": "info"
      },
      {
        "title": "Help",
        "payload": "help"
      }
    ],
    "authorTimestamp": "2024-11-04T00:00:00.000Z",
    "authorId": "user123",
    "authorFirstName": "",
    "authorLastName": "",
    "created": "2024-11-04T00:00:00.000Z"
  }
]

```

## * unemployment-rate:
### Example passed parameters
```
{
  "chatId": "12345",
  "authorId": "user123",
  "input": "2023"  # optional - default to currentYear
}
```
### Example response
```
[
  {
    "chatId": "12345",
    "content": "Viimane töötuse määr 2023. aastal on 6.5",
    "buttons": [
      {
        "title": "More Info",
        "payload": "info"
      },
      {
        "title": "Help",
        "payload": "help"
      }
    ],
    "authorTimestamp": "2024-11-04T00:00:00.000Z",
    "authorId": "user123",
    "authorFirstName": "",
    "authorLastName": "",
    "created": "2024-11-04T00:00:00.000Z"
  }
]

```

## * consumer-price-index:
### Example passed parameters
```
{
  "chatId": "12345",
  "authorId": "user123",
  "input": "previous_month, märts, 2023_2024" (optional)
        # Also accepts input parameters individually
}

```
### Example Response
```
[
  {
    "chatId": "12345",
    "content": "Consumer Price Index for 2024 in March is 2.0, based on the indicator 'inflation'.",
    "buttons": [
      {
        "title": "More Info",
        "payload": "info"
      },
      {
        "title": "Help",
        "payload": "help"
      }
    ],
    "authorTimestamp": "2024-11-04T00:00:00.000Z",
    "authorId": "user123",
    "authorFirstName": "",
    "authorLastName": "",
    "created": "2024-11-04T00:00:00.000Z"
  }
]
```
