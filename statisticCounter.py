import sys
import time
from multiprocessing.dummy import Pool

def getFilePath():
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = "10m.txt"
    return file_path

def readNumbers(file_path):
    pool = Pool(8)
    with open(file_path) as f:
        numbers = pool.map(float,f)
        pool.close()
        pool.join()
        return numbers

def findMaxNumber(numbers):
    return max(numbers)

def findMinNumber(numbers):
    return min(numbers)

def findAvarage(numbers):
    return sum(numbers)/len(numbers)

def findMedian(numbers):
    if len(numbers)%2 != 0:
        return sorted(numbers)[len(numbers)/2]
    else:
        median = (sorted(numbers)[len(numbers)/2] + sorted(numbers)[len(numbers)/2-1])/2.0
        return median

def execFindFunctions(numbers):
    print "Maximal number is: %s" % (findMaxNumber(numbers))
    print "Minimal number is: %s" % (findMinNumber(numbers))
    print "Avarage number is: %s" % (findAvarage(numbers))
    print "Median of list is: %s" % (findMedian(numbers))

if __name__ == "__main__":
    file_path = getFilePath()
    t = time.time()
    numbers = readNumbers(file_path)
    execFindFunctions(numbers)
    t = time.time() - t
    print 'The work is done in %s seconds' % (t)
