#!/bin/bash
# Send request to URL and display the status code of the response
curl -so /dev/null -w "%{http_code}" "$1"
