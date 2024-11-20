# Electricity API Documentation (GET)

### Trigger the service via Bürokratt Chatbot
```
Millal on täna odav elekter?
Millal on täna kallis elekter?
```

### Trigger the service as a stand-alone
NB! Required DSL parameters for all services
```
chatId: "${incoming.params.chatId}"
authorId: "${incoming.params.authorId}"
```

Endpoints
```
electricity/current-price       # current pice          no params
electricity/highest-price       # description           no params 
electricity/lowest-price        # lowest price today    no params
```

## * current-price
```
curl localhost:8080/electricity/current-price
```
Expected outcome
```
{
    "result": "Antud tunnil on elektri börsihind 84.3 €/mWh"
}
```

## * highest-price
```
curl localhost:8080/electricity/highest-price
```
Expected outcome
```
{
    "result": "Täna on kõrgeim elektri börsihind 385.85 €/mWh, kell 18:00"
}
```

## * lowest-price 
```
curl localhost:8080/electricity/lowest-price
```
Expected outcome
```
{
    "result": "Täna on madalaim elektri börsihind 3.82 €/mWh, kell 02:00"
}
```