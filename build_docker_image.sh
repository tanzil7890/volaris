#!/bin/bash

docker_user="your_dockerhub_username"

read -p "Do you want to build the nightly version of the volaris image? (default is stable) (yes/no): " answer;
answer=$(echo "$answer" | tr '[:upper:]' '[:lower:]')

if [ "$answer" = "yes" ]; then
    # Build the nightly version of the volaris image
    docker build --build-arg IS_STABLE=no -t volaris_image -f ./Dockerfile .
    image_tag="nightly"
else
    # Build the stable version of the volaris image
    docker build -t volaris_image -f ./Dockerfile .
    image_tag="stable"
fi

read -p "Is it uploaded to docker hub? (default is no) (yes/no): " answer;
answer=$(echo "$answer" | tr '[:upper:]' '[:lower:]')

if [ "$answer" = "yes" ]; then
    # Log in to Docker Hub
    # If you are a new docker hub user, please verify your email address before proceeding with this step.
    docker login
    # Tag the Docker image
    docker tag volaris_image "$docker_user/volaris_image:$image_tag"
    # Push the Docker image to Docker Hub
    docker push "$docker_user/volaris_image:$image_tag"
else
    echo "Not uploaded to docker hub."
fi
