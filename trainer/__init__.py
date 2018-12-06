from trainer.splitter import Splitter

if __name__ == '__main__':
    splitter = Splitter(0.8, 0.05, 0.15, "data/anarchism")
    splitter.doSplit()
