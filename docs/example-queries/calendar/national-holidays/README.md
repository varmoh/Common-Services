# National Holidays API Documentation (GET)
### Trigger the service via Bürokratt Chatbot
```
Millal on selle aasta riigipühad?
Mis on järgmised tähtsad riigipühad sel aastal?
Millal toimusid eelmised riigipühad?
Mis oli viimane riigipüha?
Mis on järgmine riigipüha?
Kas täna on riigipüha?
Mis kuupäeval on jaanipäev?
Mis riigipühad on veebruaris?
```
### Trigger the service as a stand-alone
NB! Required DSL parameters for all services
```
chatId: "${incoming.params.chatId}"
authorId: "${incoming.params.authorId}"
```

Endpoints
```
| Endpoint                                             | Description                                        | Parameters                                        |
|------------------------------------------------------|----------------------------------------------------|---------------------------------------------------|
| `calendar/national-holidays/eoy`                     | Current day → end of year                          | No parameters                                     |
| `calendar/national-holidays/national-holidays`       | All national holidays                              | No parameters                                     |
| `calendar/national-holidays/next`                    | Current day → next holiday                         | No parameters                                     |
| `calendar/national-holidays/previous`                | Current day → previous nearest holiday             | No parameters                                     |
| `calendar/national-holidays/today`                   | Is today a national holiday?                       | No parameters                                     |
| `calendar/national-holidays/ytd`                     | January → current month                            | No parameters                                     |
| `calendar/national-holidays/find/by-name`            | Find holiday by name                               | Accepts `incoming.params.input` (e.g. “jaanipäev”) |
| `calendar/national-holidays/find/by-month`           | Find holidays by month                             | Accepts `incoming.params.input` (e.g. “juuni”)    |

```

# * eoy
```
curl localhost:8080/calendar/national-holidays/eoy
```
Expected outcome - if current date e.g. "2024-09-24"
```
{
    "result": "Kõik riigipühad alates tänsest kuni aasta lõpuni on: \n*2024-12-24\n jõululaupäev\n\n *2024-12-25\n esimene jõulupüha\n\n *2024-12-26\n teine jõulupüha\n\n"
}
```

# * national-holidays
```
curl localhost:8080/calendar/national-holidays/national-holidays
```
Expected outcome
```
{
    "result": "Kõik pühad sellel aastal on:\n * 2024-01-01\nuusaasta\n\n * 2024-02-24\niseseisvuspäev, Eesti Vabariigi aastapäev\n\n * 2024-03-29\nsuur reede\n\n * 2024-03-31\nülestõusmispühade 1. püha\n\n * 2024-05-01\nkevadpüha\n\n * 2024-05-19\nnelipühade 1. püha\n\n * 2024-06-23\nvõidupüha\n\n * 2024-06-24\njaanipäev\n\n * 2024-08-20\ntaasiseseisvumispäev\n\n * 2024-12-24\njõululaupäev\n\n * 2024-12-25\nesimene jõulupüha\n\n * 2024-12-26\nteine jõulupüha\n\n"
}
```

# * next
```
curl localhost:8080/calendar/national-holidays/next
```
Expected outcome - if current date e.g. "2024-09-24"
```
{
    "result": "Tulev riigipüha on jõululaupäev - 2024-12-24"
}
```

# * previous
```
curl localhost:8080/calendar/national-holidays/previous
```
Expected outcome - if current date e.g. "2024-09-24"
```
{
    "result": "Viimane riigipüha oli taasiseseisvumispäev - 2024-08-20"
}
```

# * today
```
curl localhost:8080/calendar/national-holidays/today
```

Expected outcome - if current date "2024-03-29"
```
{
    "result": "Täna on suur reede"
}
```

# * ytd
```
curl localhost:8080/calendar/national-holidays/ytd
```

Expected outcome - if current date e.g. "2024-09-24"
```
{
    "result": "Kõik pühad aasta algusest kuni tänaseni:\n* 2024-01-01\nuusaasta\n\n* 2024-02-24\niseseisvuspäev, Eesti Vabariigi aastapäev\n\n* 2024-03-29\nsuur reede\n\n* 2024-03-31\nülestõusmispühade 1. püha\n\n* 2024-05-01\nkevadpüha\n\n* 2024-05-19\nnelipühade 1. püha\n\n* 2024-06-23\nvõidupüha\n\n* 2024-06-24\njaanipäev\n\n* 2024-08-20\ntaasiseseisvumispäev\n"
}
```

# * find/by-name
```
curl localhost:8080/calendar/national-holidays/by-name?input=jaanipäev
```

Expected outcome
```
{
    "result": "Jaanipäev on 2024-06-24"
}
```

if no match found
```
{
    "result": "Ei leia sellist riigipüha"
}
```

# * find/by-month
```
curl /calendar/national-holidays/find/by-month?input=juuni
```

Expected outcome
```
{
    "result": "Kõik riigipühad antud kuus on: \n*2024-06-23\n võidupüha\n\n*2024-06-24\n jaanipäev\n\n"
}
```

default: current month - if no value given
```
{
    "result": "Kõik riigipühad antud kuus on: \n*2024-08-20\n taasiseseisvumispäev\n\n"
}
```

if no match found
```
{
    "result": "Ei leia riigipühi antud kuus"
}
```
