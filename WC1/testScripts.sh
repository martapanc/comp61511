#!/bin/bash

echo "*** TEST RESULTS ***"
echo "miniwc.py: "
python3 miniwc.py $1

echo "miniwc_w_characters.py:"
python3 miniwc_w_characters.py $1

echo "wc:"
wc $1

echo "wc -m:"
wc -m $1
