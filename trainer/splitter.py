import sys
import json
import random


class Splitter:
    """Split a given Corpora to a training, validation and testing set."""

    def __init__(self, training_set_ratio, validation_set_ratio, testing_set_ratio, input_file_address):
        self.trainingSetRatio = training_set_ratio
        self.validationSetRatio = validation_set_ratio
        self.testingSetRatio = testing_set_ratio
        self.inputFileAddress = input_file_address
        self.size = None
        self.testingSet = list()
        self.trainingSet = list()
        self.validationSet = list()

    def doSplit(self):
        print("Starting to split the sets...")
        comments = list()
        with open(self.inputFileAddress) as subreddit:
            for line in subreddit:
                comments.append(json.loads(line))
            random.shuffle(comments)
            self.size = len(comments)
            train_set_size = round(self.size * self.trainingSetRatio)
            test_set_size = round(self.size * self.testingSetRatio)
            valid_set_size = round(self.size * self.validationSetRatio)
            for i in range(0, train_set_size):
                self.trainingSet.append(comments[i])
            for i in range(0, test_set_size):
                self.testingSet.append(comments[i])
            for i in range(0, valid_set_size):
                self.validationSet.append(comments[i])
        subreddit.close()

    def saveSets(self):
        train = open(self.inputFileAddress + "_train.txt", "w+")
        valid = open(self.inputFileAddress + "_valid.txt", "w+")
        test = open(self.inputFileAddress + "_test.txt", "w+")
        for comment in self.trainingSet:
            train.write(comment['body'] + '\n')
        for comment in self.validationSet:
            valid.write(comment['body'] + '\n')
        for comment in self.testingSet:
            test.write(comment['body'] + '\n')
        train.close()
        valid.close()
        test.close()

if __name__ == '__main__':
    normalized = sys.argv[1]
    splitter = Splitter(0.8, 0, 0.2, normalized)
    splitter.doSplit()
    print("Splitting finished!")
    splitter.saveSets()
    print("Sets saved!")
