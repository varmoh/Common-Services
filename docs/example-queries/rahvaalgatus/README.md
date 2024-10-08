# Rahvaalgatus Service API Documentation
## Service to get 5 most-popular or 5 most-recent initiatives

#### Endpoints

```
rahvaalgatus/mock/most-popular
rahvaalgatus/mock/most-recent 
rahvaalgatus/most-popular
rahvaalgatus/most-recent
```

#### Sample query

```
curl localhost:8080/rahvaalgatus/mock/most-popular
```
```
curl localhost:8080/rahvaalgatus/most-popular
```
#### Expected outcome
```
{
    "response": [
        {
            "id": "b358b3a7-a131-4bb4-9647-bc6e6c8c8044",
            "for": "parliament",
            "title": "Tasuta kõrghariduse säilitamine",
            "phase": "sign",
            "signingEndsAt": "2024-10-18T21:00:00.000Z",
            "signatureCount": 7242,
            "signatureThreshold": 1000
        },
        ...
        {
            "id": "77f4a769-f33f-45fa-88e9-6368d94d22c4",
            "for": "parliament",
            "title": "Lapsi toetav nutiseadmekasutuse reguleerimine Eesti koolidesse!",
            "phase": "sign",
            "signingEndsAt": "2025-02-24T22:00:00.000Z",
            "signatureCount": 1673,
            "signatureThreshold": 1000
        }
    ]
}
```

#### Sample query

```
curl localhost:8080/rahvaalgatus/mock/most-recent
```
```
curl localhost:8080/rahvaalgatus/most-recent
```
#### Expected outcome
```
{
    "response": [
        {
            "id": "f799449f-d1e6-4ecf-a326-cf870ef36a54",
            "for": "kose-vald",
            "title": "Toetusavaldus Piret Sappi jätkamiseks Ardu kooli ja lasteaia juhina",
            "phase": "government",
            "signingEndsAt": "2024-10-04T21:00:00.000Z",
            "signatureCount": 138,
            "signatureThreshold": 59
        },
        ...
        {
            "id": "dfa755b6-9db6-43f6-91cf-f8cb6c7c7b8f",
            "for": "rae-vald",
            "title": "Rae valla lastehoiu lisakulude hüvitamise määrus",
            "phase": "sign",
            "signingEndsAt": "2024-11-30T22:00:00.000Z",
            "signatureCount": 250,
            "signatureThreshold": 163
        }
    ]
}
```

