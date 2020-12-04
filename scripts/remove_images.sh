#!/bin/bash

# Script finding all <none> Docker images and removing them
# First it finds all related containers, stops them and removes them.
# After removing containers, images can be safely stopped.

images=$(docker images -a | awk '{ print $1,$3 }')

echo $images

exit 0

if [ "$images" == "" ]; then
    echo "No images found."
    exit 0
fi


for image in $images; do
   
    echo "Image: $image"

    # Find containers usibng image
    containers=$(docker ps -a | awk '{ print $1,$2 }' | grep $image)
    
    if [ "$containers" == "" ]; then
        echo "No containers to stop"
        continue
    fi
    
    echo "Used by containers:"
    
    # Stop & remove all found containers
    for container in $containers; do
        echo "-> $container"
     	docker container stop $container
	    docker container rm $container
    done
    
    # Remove image
    docker rmi $image
done
