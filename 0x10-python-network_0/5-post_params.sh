#!/bin/bash
# Takes URL, sends POST request and displays body of response
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" -X POST "$1"
