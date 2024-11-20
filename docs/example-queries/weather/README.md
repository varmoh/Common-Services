# Weather API Documentation (POST)

### Trigger the service via Bürokratt Chatbot
```
Mis ilm on Tallinnas?
Mis ilm on Pärnus?
Mis ilm on Paides?
```

### Trigger the service as a stand-alone
NB! Required DSL parameters for all services
```
chatId: "${incoming.body.chatId}"
authorId: "${incoming.body.authorId}"
```

Endpoints
```
weather/EE    #accepts params (e.g incoming.body.input = "paide")
```


## * EE
```
curl -X POST http://localhost:8080/weather/EE -d '{"chatId": "123", "authorId": "abc123", "input": "paide"}'
```
Expected outcome
```
{
    "result": "Hetkel on õhutemperatuur 4.8°C (tajutav 0.6°C), puhub tuul 5.1m/s."
}
```