#!/bin/bash

#Simple script for testing the miniWc functionality compared to the real WC

echo "*** TEST RESULTS ***"
echo "miniwc.py: "
python3 miniwc.py $1

echo "miniwc_w_characters.py:"
python3 Challenges/miniwc_w_characters.py $1

echo "wc:"
wc $1

echo "wc -m:"
wc -m $1
