# Statistics-Estonia API Documentation GET


### Trigger the service via Bürokratt Chatbot
```
Consumer Price Index:
    Mis on tarbija indeks?
    Mis on tarbija indeks 2021?
    Mis on tarbija indeks 2021 jaanuaris?

Estimated Subsistence Minimum:
    Arvestuslik elatusmiinimum

Unemployment Rate:
    Mis on töötuse määr Eestis?
    Mis on töötuse määr aastal 2021 Eestis?
```


### Trigger the service as a stand-alone
NB! Required DSL parameters for all services
```
chatId: "${incoming.params.chatId}"
authorId: "${incoming.params.authorId}"
```

Endpoints
```
statistics-estonia/consumer-price-index    # accepts params (e.g incoming.params.input = "previous_month,veebruar,2023")
statistics-estonia/estimated-subsistence-minimum    # no params
statistics-estonia/unemployment-rate       #  # accepts params (e.g incoming.params.input = "2022")
```


## * consumer-price-index 
```
curl localhost:8080/statistics-estonia/consumer-price-index?input=previous_year,veebruar,2023
```
Expected outcome
```
{
    "result": "Tarbijahinnaindeks võrreldes 2023. aastale eelneva aasta sama 
    kuuga\\n\\n2023\\nveebruar: 17.6%"
}
```

## * estimated-subsistence-minimum 
```
curl localhost:8080/statistics-estonia/estimated-subsistence-minimum
```
Expected outcome
```
{
    "result": "Arvestuslik elatusmiinimum 2023. aastal on 338.23 €/kuus"
}
```

## * unemployment-rate
```
curl localhost:8080/statistics-estonia/unemployment-rate?input=2021
```
Expected outcome
```
{
    "result": "2021. aastal oli Eestis töötuse määr 6.5%"
}
```