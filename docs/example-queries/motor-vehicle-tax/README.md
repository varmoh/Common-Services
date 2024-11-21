# Motor Vehicle Tax API Documentation GET

### Trigger the service via Bürokratt Chatbot
```
# trigger questions
```

### Trigger the service as a stand-alone
NB! Required DSL parameters for all services
```
chatId: "${incoming.params.chatId}"
authorId: "${incoming.params.authorId}"
```

Endpoints
```
motor-vehicle-tax/registration-number   #tax by reg number  #e.g. incoming.params.input="430MEN"
```


## * registration-number
```
curl localhost:8080/motor-vehicle-tax/registration-number?input=430MEN
```
Expected outcome
```
{
    "result": "Sõiduki 430MEN aastamaks on kokku 419.30€\\nMillest baasosa on 50.00€,\\nCO₂ eriheite osa on 285.42€\\nmassiosa on 83.88€\\n\\nRegistreerimistasu tuleb 1681.71€\\nMillest baasosa on 150.00€\\nCO₂ eriheite osa on 1337.65€\\nmassiosa on 194.06€\\n"
}
```