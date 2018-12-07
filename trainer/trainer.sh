#!/bin/bash
# $1 is the address of fasttext repository.
# $2 is the address of train set
# $3 is the address of test set
train=$2
testSet=$3
for j in `seq 1 5`;
do
        for k in 1 2 3;
        do
                let "DIM = $j * 50"
                name="model_dim$DIM-ngram$k"
                echo "$name..."
                echo "Model $name.bin - DIM: $DIM: - Ngrams: $k" &>> ../data/output/report.txt
                $1 sent2vec -input "$train" -output "../data/models/$name" -lr $LR -dim $DIM -wordNgrams $k &>> ../data/output/report.txt
                echo "Learned..."
                cat "$testSet" | $1 print-sentence-vectors "../data/models/$name.bin" &>> "./output/$name.txt"
                echo "=====================================================================================================================\n"&>> ./output/report.txt
                echo "And Tested..."
                #rm "./models/$name.bin"
                #echo "And also removed!"
        done
done
