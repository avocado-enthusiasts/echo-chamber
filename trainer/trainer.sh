#!/bin/bash
# $1 is the address of fasttext repository.
# $2 is the address of train set
# $3 is the address of test set
# $4 is the name of the category
train=$2
testSet=$3
for j in 2 10 50 100 140 700;
do
        for k in 1 2 3;
        do
                let "DIM = $j * 50"
                name="$4_model_dim$DIM-ngram$k"
                echo "$name..."
                echo "Model $name.bin - DIM: $DIM: - Ngrams: $k" &>> ../output/results/report.txt
                $1 sent2vec -input "$train" -output "../output/models/$name" -dim $DIM -wordNgrams $k &>> ../output/results/report.txt
                echo "Learned..."
                cat "$testSet" | $1 print-sentence-vectors "../output/models/$name.bin" &>> "../output/vectors/$name.txt"
                echo "========================================================================\n"&>> ../output/results/report.txt
                echo "And Tested..."
                #rm "./models/$name.bin"
                #echo "And also removed!"
        done
done
