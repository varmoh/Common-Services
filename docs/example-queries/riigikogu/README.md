# Riigikogu API Documentation (GET)


### Trigger the service via Bürokratt Chatbot
```
Mis oli riigikogu viimane hääletus?
Mis on viimased hääletused parlamendis?
Parlamendi liikme kohalolu Mart Helme?
```


### Trigger the service as a stand-alone
NB! Required DSL parameters for all services
```
chatId: "${incoming.params.chatId}"
authorId: "${incoming.params.authorId}"
```

Endpoints
```
riigikogu/five-most-recent         # 5 most recent voting results         no params
riigikogu/members-participation    # 5 participation statistics           input: memberName
riigikogu/recent-voting            # recent voting result                 no params
```
---------------------------------------------------------------------------------------------

## * five-most-recent  
```
curl localhost:8080/riigikogu/five-most-recent
```
Expected outcome
```
{
    "result": "Viis viimast hääletustulemust:\\n 1. Meditsiiniseadme seaduse muutmise ja sellega seonduvalt teiste 
    seaduste muutmise seadus (pädevuse andmine Ravimiametile)\\n Kohal: 86\\n Puudus: 15\\n Poolt: 65\\n Vastu: 0\\n 
    Erapooletu: 1\\n Ei hääletanud: 35\\n\\n 2. Ravimiseaduse ja tervishoiuteenuste korraldamise seaduse muutmise 
    seadus\\n Kohal: 86\\n Puudus: 15\\n Poolt: 63\\n Vastu: 0\\n Erapooletu: 1\\n Ei hääletanud: 37\\n\\n ...\n"
}
```

## * members-participation
```
curl localhost:8080/riigikogu/members-participation?input=jaak
```
Expected outcome
```
{
    "result": "Jaak Aab on aastal 2024 osalenud istungitel 98 korda ja puudunud 9 korda."
}
```

## * recent-voting 
```
curl localhost:8080/riigikogu/recent-voting
```
Expected outcome
```
{
    "result": "Viimane hääletus:\\n\\nMeditsiiniseadme seaduse muutmise ja sellega seonduvalt teiste seaduste muutmise 
    seadus (pädevuse andmine Ravimiametile)\\n\\nKohal: 86\\nPuudus: 15\\nPoolt: 65\\nVastu: 0\\nErapooletu: 1\\nEi 
    hääletanud: 35"
}
```