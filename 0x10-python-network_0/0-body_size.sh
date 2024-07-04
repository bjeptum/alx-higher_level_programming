#!/bin/bash
# Send request to URL and outputs size of body
curl -sI "$1" | grep -i content-length | awk '{print $2}'
