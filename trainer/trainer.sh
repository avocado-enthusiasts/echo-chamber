#!/bin/bash
# $1 is the address of fasttext repository.
for i in 1 5 9;
do
        for j in `seq 1 5`;
        do
                for k in 1 2 3;
                do
                        LR="0.$i"
                        let "DIM = $j * 50"
                        name="model_lr$LR-dim$DIM-ngram$k"
                        echo "$name..."
                        echo "Model $name.bin - LR: $LR - DIM: $DIM: - Ngrams: $k" &>> ../data/output/report.txt
                        $1 sent2vec -input ../data/train.txt -output "../data/models/$name" -lr $LR -dim $DIM -wordNgrams $k &>> ../data/output/report.txt
                        echo "Learned..."
                        cat "../data/test.txt" | $1 print-sentence-vectors "../data/models/$name.bin" &>> "./output/$name.txt"
                        echo "=====================================================================================================================\n"&>> ./output/report.txt
                        echo "And Tested..."
                        rm "./models/$name.bin"
                        echo "And also removed!"
                done
        done
done
