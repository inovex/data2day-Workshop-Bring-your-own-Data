#!/bin/bash

# Variables
source ./00-variables.sh

# Ensure Podman is installed and running
if ! podman info > /dev/null 2>&1; then
    echo "Podman is not installed or running. Please install/start Podman and try again."
    exit 1
fi

echo ""
echo "========================================================"
echo " Building the chat app container with version $tag"
echo "========================================================"
echo ""
podman build -t ${chatImageName}:$tag -f Dockerfile --build-arg FILENAME=app.py --build-arg PORT=$port .

# Tag the image with ACR repository name
podman tag ${chatImageName}:$tag testregistry1234.azurecr.io/${chatImageName}:$tag

echo ""
echo "========================================================"
printf 'Do you want to push the image (y/n)? '
read answer

if [ "$answer" != "${answer#[Yy]}" ] ;then
    # Log in to ACR using Podman
    echo "Logging in to ACR..."
    TOKEN=$(az acr login --name ${acrName} --expose-token | jq -r '.accessToken')
    if [ -z "$TOKEN" ]; then
        echo "Failed to retrieve access token."
        exit 1
    fi

    podman login ${acrLoginServer} --username 00000000-0000-0000-0000-000000000000 --password $TOKEN
    if [ $? -ne 0 ]; then
        echo "Failed to log in to ACR."
        exit 1
    fi

    # Push the image to ACR
    echo "Pushing the image to ACR..."
    podman push ${acrLoginServer}/${chatImageName}:$tag
    if [ $? -ne 0 ]; then
        echo "Failed to push the image to ACR."
        exit 1
    fi

else
    exit
fi