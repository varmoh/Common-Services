#!/bin/bash

URL=$1
AUTH=$2
MOCK_ALLOWED=${3:-false}

if [[ -z $URL || -z $AUTH ]]; then
  echo "Url and Auth are required"
  exit 1
fi

# Clear Pipelines
curl -XDELETE "$URL/_ingest/pipeline/*" -u "$AUTH" --insecure

# Companies
curl -XDELETE "$URL/companies?ignore_unavailable=true" -u "$AUTH" --insecure
curl -H "Content-Type: application/x-ndjson" -X PUT "$URL/companies" -ku "$AUTH" --data-binary "@fieldMappings/companies.json"
curl -L -X POST "$URL/_scripts/company-with-name" -H 'Content-Type: application/json' -H 'Cookie: customJwtCookie=test' --data-binary "@templates/company-with-name.json"
curl -L -X POST "$URL/_scripts/company-employees-with-code" -H 'Content-Type: application/json' -H 'Cookie: customJwtCookie=test' --data-binary "@templates/company-employees-with-code.json"
curl -L -X POST "$URL/_scripts/companies-employees-with-county" -H 'Content-Type: application/json' -H 'Cookie: customJwtCookie=test' --data-binary "@templates/companies-employees-with-county.json"
curl -L -X POST "$URL/_scripts/companies-employees" -H 'Content-Type: application/json' -H 'Cookie: customJwtCookie=test' --data-binary "@templates/companies-employees.json"
curl -L -X PUT "$URL/_ingest/pipeline/convert-employees-to-int" -H 'Content-Type: application/json' -H 'Cookie: customJwtCookie=test' --data-binary "@pipelines/convert-employees-to-int.json"
if $MOCK_ALLOWED; then curl -H "Content-Type: application/x-ndjson" -X PUT "$URL/companies/_bulk?pipeline=convert-employees-to-int" -ku "$AUTH" --data-binary "@mock/companies.json"; fi
