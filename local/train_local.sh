#!/bin/sh

if [ "$*" == "" ]; then
    echo "No algorithm provided"
    exit 1
fi

ALGO=$1

mkdir -p test_dir/model
mkdir -p test_dir/output

rm test_dir/model/*
rm test_dir/output/*

docker run -v $(pwd)/test_dir:/opt/ml --rm $ALGO train
