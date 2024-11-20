# Public-Initiatives API Documentation (GET)


### Trigger the service via Bürokratt Chatbot
```
Mis on hetkel populaarsemad rahvaalgatused?
Mis on viis viimast avalikku algatust?
```


### Trigger the service as a stand-alone
NB! Required DSL parameters for all services
```
chatId: "${incoming.params.chatId}"
authorId: "${incoming.params.authorId}"
```

Endpoints
```
public-initiatives/most-popular    # 5 most popular initiatives    no params
public-initiatives/most-recent     # 5 most recent initiatives     no params
```


## * most-popular
```
curl localhost:8080/public-initiatives/most-popular
```
Expected outcome
```
{
    "result": "Viis populaarsemat aktiivset algatust:\\n
    1. Lapsi toetav nutiseadmekasutuse reguleerimine Eesti koolidesse!\\n
      Kogutud allkirjad: 1924 / min. allkirjad: 1000\\n\\n
    2. Eesti toetab Palestiina omariiklust\\n
      Kogutud allkirjad: 1308 / min. allkirjad: 1000\\n\\n
    3. Tallinna lasteaedades tuleb kaotada kohatasu\\n
      Kogutud allkirjad: 1235 / min. allkirjad: 3518\\n\\n
    4. Petitsioon uimastitarvitamise eest määratavate karistuste leevendamiseks\\n
      Kogutud allkirjad: 1069 / min. allkirjad: 1000\\n\\n
    5. Kaitseme lapse õigust mõlemale vanemale\\n
      Kogutud allkirjad: 942 / min. allkirjad: 1000"
}
```

## * most-recent
```
curl localhost:8080/public-initiatives/most-recent
```
Expected outcome
```
{
    "result": "Viis viimast aktiivset algatust:\\n
    1. Säilitame Tõrva Kõrtsihoone ajaloolise välimuse!\\n
       Kogutud allkirjad: 77 / min. allkirjad: 49\\n\\n
    2. Nõuame Lasnamäe jaoks hädavajaliku bussiliini nr 65 säilitamist!\\n
       Kogutud allkirjad: 3764 / min. allkirjad: 3518\\n\\n
    3. Palume lõpetada detailplaneering raadiosidemasti paigaldamiseks, et säilitada Urmi küla ainulaadne looduslik ja kultuuriline keskkond.\\n
       Kogutud allkirjad: 135 / min. allkirjad: 116\\n\\n
    4. Kuldala pargi säilitamine\\n
       Kogutud allkirjad: 614 / min. allkirjad: 159\\n\\n
    5. Tuld talveajale\\n
       Kogutud allkirjad: 229 / min. allkirjad: 1000"
}
```