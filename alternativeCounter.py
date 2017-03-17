import sys
import time
import numpy as np
from multiprocessing.dummy import Pool

def getFilePath():
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = "10m.txt"
    return file_path

def readNumbers(file_path):
    pool = Pool(4)
    with open(file_path) as f:
        numbers = pool.map(float,f)
        pool.close()
        return numbers

def sortNumbers(numbers):
    return np.sort(numbers)

def findMaxNumber(numbers,length):
    return numbers[length - 1]

def findMinNumber(numbers):
    return numbers[0]

def findAvarage(numbers,length):
    return np.sum(numbers) / length

def findMedian(numbers,length):
    if length % 2 != 0:
        return numbers[length / 2]
    else:
        return (numbers[length / 2] + numbers[(length / 2) - 1]) / 2

def execFindFunctions(numbers):
    numbers = sortNumbers(numbers)
    length = np.alen(numbers)
    print "Maximal number is: %s" % (findMaxNumber(numbers,length))
    print "Minimal number is: %s" % (findMinNumber(numbers))
    print "Avarage number is: %s" % (findAvarage(numbers,length))
    print "Median of list is: %s" % (findMedian(numbers,length))

if __name__ == "__main__":
    t = time.time()
    file_path = getFilePath()
    numbers = readNumbers(file_path)
    execFindFunctions(numbers)
    t = time.time() - t
    print 'The work is done in %s seconds' % (t)
