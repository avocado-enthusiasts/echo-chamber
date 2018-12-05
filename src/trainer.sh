#!/bin/bash
for i in 1 4 7;
do
        for j in `seq 1 5`;
        do
                for k in 1 2 3;
                do
                        LR="0.$i"
                        let "DIM = $j * 50"
                        name="mlr$LR-dim$DIM-gram$k"
                        echo "$name..."
                        echo "Model $name.bin - LR: $LR - DIM: $DIM: - Ngrams: $k" &>> ./output/report.txt
                        ../fasttext sent2vec -input train.txt -output "./models/$name" -lr $LR -dim $DIM -wordNgrams $k &>> ./output/report.txt
                        echo "Learned..."
                        cat "test.txt" | ../fasttext print-sentence-vectors "./models/$name.bin" &>> "./output/$name.txt"
                        echo "=====================================================================================================================\n"&>> ./output/report.txt
                        echo "And Tested..."
                        rm "./models/$name.bin"
                        echo "And also removed!"
                done
        done
done
