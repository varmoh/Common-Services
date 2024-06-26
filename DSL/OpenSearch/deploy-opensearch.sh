#!/bin/bash

URL=$1
AUTH=$2
MOCK_ALLOWED=${3:-false}

if [[ -z $URL || -z $AUTH ]]; then
  echo "Url and Auth are required"
  exit 1
fi

# Companies
curl -XDELETE "$URL/companies?ignore_unavailable=true" -u "$AUTH" --insecure
curl -H "Content-Type: application/x-ndjson" -X PUT "$URL/companies" -ku "$AUTH" --data-binary "@fieldMappings/companies.json"
curl -L -X POST "$URL/_scripts/company-with-name" -H 'Content-Type: application/json' -H 'Cookie: customJwtCookie=test' --data-binary "@templates/company-with-name.json"
if $MOCK_ALLOWED; then curl -H "Content-Type: application/x-ndjson" -X PUT "$URL/companies/_bulk" -ku "$AUTH" --data-binary "@mock/companies.json"; fi
