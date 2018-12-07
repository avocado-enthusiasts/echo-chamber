import os
import sys
import numpy

def main():
    for filename in os.listdir(sys.argv[1]):
        if filename.endswith(".npy"):
            vectors = numpy.load(sys.argv[1] + filename)
            mean = vectors.mean(0)
            numpy.save(sys.argv[1] + "mean" + filename, mean)
            max = vectors.max(0)
            numpy.save(sys.argv[1] + "max" + filename, max)
            min = vectors.min(0)
            numpy.save(sys.argv[1] + "min" + filename, min)
        else:
            continue

if __name__ == '__main__':
    main()