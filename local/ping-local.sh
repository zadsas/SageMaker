#!/bin/bash

# local setup: ./ping-local.sh $(docker-machine ip)
# jupyter terminal: ./ping-local.sh

HOST_IP=${1:-localhost}
curl -v http://$HOST_IP:8080/ping
