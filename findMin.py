import time
from random import randrange

#def findMin(alist):
#    overallMin = alist[0]
#    for i in alist:
#        issmallest = True
#        for j in alist:
#            if i > j:
#                issmallest = False
#        if issmallest:
#            overallMin = i
#    return overallMin

#print(findMin([5,4,2,6,1]))
#print(findMin([1,3,7,6,4]))

def findMin(alist):
    minsofar = alist[0]
    for i in alist:
        if i < minsofar:
            minsofar = i
    return minsofar

print(findMin([5,4,2,6,1]))
print(findMin([1,3,7,6,4]))

for listsize in range(1000,10001,1000):
    alist = [randrange(10000) for x in range(listsize)]
    start = time.time()
    findMin(alist)
    end = time.time()
    print("size: %d time %f" % (listsize, end-start))

#from random import randrange
#for listsize in range(1,10,2):
#    alist = [randrange(10) for x in range(listsize)]
#    print(alist)