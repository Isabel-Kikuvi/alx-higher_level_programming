#!/bin/bash
#Send GET request to a URL and displays size of body of the response
curl -s "$1" | wc -c
