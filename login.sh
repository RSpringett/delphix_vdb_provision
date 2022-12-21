#!/bin/bash
curl -s -X POST -k --data @- http://10.44.1.160/resources/json/delphix/session \
   -c "cookies.txt" -H "Content-Type: application/json" <<EOF
{
   "type": "APISession",
   "version": {
       "type": "APIVersion",
       "major": 1,
       "minor": 11,
       "micro": 14
  }
}
EOF

curl -s -X POST -k --data @- http://10.44.1.160/resources/json/delphix/login \
-b "cookies.txt" -c "cookies.txt" -H "Content-Type: application/json" <<EOF
{
"type": "LoginRequest",
"username": "admin",
"password": "fwdview01!"
}
EOF