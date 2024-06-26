# Common Services

Bürokratt Common Services that can be used both with and without Bürokratt chat

## Dev setup

- Clone [Ruuter](https://github.com/buerokratt/Ruuter)
- Navigate to Ruuter dev branch and build the image `docker build -t ruuter .`
- Clone [Data Mapper](https://github.com/buerokratt/DataMapper)
- Navigate to Data Mapper dev branch and build the image `docker build -t data-mapper .`
- Clone [Cron Manager](https://github.com/buerokratt/CronManager.git)
- Navigate to Cron Manager dev branch and build the image `docker build -t cron-manager .`

### Open Search

- To Initialize Open Search run `./deploy-opensearch.sh <URL> <AUTH> <Is Mock Allowed - Default false>`
- To Use Opensearch locally run `./deploy-opensearch.sh http://localhost:9200 admin:admin true`

### Notes

##### Ruuter Internal Requests

- When running ruuter either on local or in an environment make sure to adjust `- application.internalRequests.allowedIPs=127.0.0.1,{YOUR_IPS}` under ruuter environments
