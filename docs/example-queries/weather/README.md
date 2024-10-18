# Weather Service API Documentation
## Estonian-specific weather information. 

**Endpoint**
```
/services/weather/EE
```

**Service accepts parameters**
```
countryCode # not required - defaults to "EE"
region      # Required! - otherwise returns error
```

**Sample query**
```
curl -X POST "http://localhost:8080/weather/EE?region=tallinn" -H "Content-Type: application/json"
```

**Expected outcome**

```
{
    "response": [
        {
            "LaiusMinut": "28",
            "Time": "2024-10-02T15:00:00.000+03:00",
            "paring": "999",
            "wl1ha": "5.000",
            "tuulekylm": "9,4",
            ...
            "sunrise": "2024-10-02T05:29:38Z",
            "sunset": "2024-10-02T16:50:43Z",
            "sunrise_eet": "2024-10-02T07:29:38.000+03:00",
            "sunset_eet": "2024-10-02T18:50:43.000+03:00",
            "location": {
                "long_address": "Harju maakond, Tallinn, Kesklinna linnaosa",
                "county": "Harju maakond",
                "county_ehak": "37"
            }
        }
    ]
}
```