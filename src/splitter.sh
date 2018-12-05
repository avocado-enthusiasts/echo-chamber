#!/bin/bash
lines=($(wc -l data/corpora.txt))
echo "Lines: $lines"
let "trainSize = (( $lines * 8 ) / 10 ) + 1"
echo "Training Size: $trainSize"
let "testSize = (( $lines * 2 ) / 10 ) + 1"
echo "Test Size: $testSize"
head -n $trainSize corpora.txt > "data/train.txt"
tail -n $testSize corpora.txt > "data/test.txt"
