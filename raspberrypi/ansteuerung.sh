#!/bin/bash
COUNTER=0
while [  $COUNTER -lt 1000 ]; do
    gpio read 29
    let COUNTER=COUNTER+1 
    sleep .01
done
