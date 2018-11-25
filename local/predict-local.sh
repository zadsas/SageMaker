#!/bin/bash

# local setup: ./predict-local.sh kmeans-request.csv $(docker-machine ip)
# jupyter terminal: ./predict-local.sh kmeans-request.csv

REQUEST_BODY=$1
HOST_IP=${2:-localhost}
curl -v -H "Content-Type: text/csv" http://$HOST_IP:8080/invocations --data-binary @$REQUEST_BODY
