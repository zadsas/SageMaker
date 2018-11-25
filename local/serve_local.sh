#!/bin/sh

if [ "$*" == "" ]; then
    echo "No algorithm provided"
    exit 1
fi

ALGO=$1

docker run -v $(pwd)/test_dir:/opt/ml -p 8080:8080 --rm $ALGO serve
