#!/bin/sh

chmod +x files/train
chmod +x files/serve

docker build  -t lstm .