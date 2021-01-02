#!/bin/bash

# Script finding all <none> Docker images and removing them
# First it finds all related containers, stops them and removes them.
# After removing containers, images can be safely stopped.

images=$(docker images -a | awk '{if(NR>1)print}' | awk '{ print $3 }')

if [ "$images" == "" ]; then
    echo "No images found."
    exit 0
fi

for image_id in $images; do
    
    image_name=$(docker images -a | awk '{if(NR>1)print}' | grep $image_id | awk '{ print $1 }')
    
    if [ "$image_name" = "<none>" ]; then
        continue
    fi

    
    if [ "$image_name" = "mysql" ]; then
        echo "Skipping mysql image and not removing any containers associated with it"
        continue
    fi

    if [ "$image_name" = "python" ]; then
        echo "Skipping python image and not removing any containers associated with it"
        continue
    fi

    if [ "$image_name" = "redis" ]; then
        echo "Skipping redis image and not removing any containers associated with it"
        continue
    fi

    echo "Image: $image_name id: $image_id"
    
    # Find containers using image
    containers=$(docker ps -a | awk '{ print $1,$2 }' | grep $image_id)
    
    if [ "$containers" == "" ]; then
        docker rmi -f $image_id
        continue
    else
        echo "Used by containers:"
    
        # Stop & remove all found containers
        for container in $containers; do
            echo "-> $container"
     	    docker container stop $container
	        docker container rm $container
        done
    fi

done

echo "Removed all images and their containers (skipped mysql)".
