#!/bin/bash

if [[ -d "../api/persistence" ]]
then
    echo "Unlocking ../api/persistence using sudo"
    sudo chown -R 1000:1000 ../api/persistence
fi
