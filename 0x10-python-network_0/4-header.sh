#!/bin/bash
# Sends GET Request with header variable with specified value 
curl -s -H "X-School-User-Id: 98" "$1"
