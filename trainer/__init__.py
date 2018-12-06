from trainer.preprocessor import Strip
from trainer.splitter import Splitter
import json

if __name__ == '__main__':
    corpora = "data/corpora"
    normalized = "data/normalized"
    tease = Strip()
    print("Starting...")
    output = open(normalized, "w+")
    with open(corpora) as textSet:
        i = 0
        for line in textSet:
            clean_comment = tease.removeAllJSON(json.loads(line), 'body')
            json.dump(clean_comment, output)
            output.write('\n')
            print("Cleaned comment #" + str(i))
            i += 1
    textSet.close()
    output.close()
    print("Cleaning finished!")
    splitter = Splitter(0.8, 0, 0.2, normalized)
    splitter.doSplit()
    print("Splitting finished!")
    splitter.saveSets()
    print("Sets saved!")
