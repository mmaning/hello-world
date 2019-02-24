#Given a list of numbers in random order, 
# write an algorithm that works in O(nlog(n)) to find the kth smallest number in the list.
import time
import random
def findnum (n, k):
    nlist = [random.randrange(10000) for x in range(n)] 
    nlist.sort()
#    print(nlist)
    print(nlist[k])

findnum(10, 2)

#def findnum1 (n, k):
    #nlist = [random.randrange(10000) for x in range(n)] 
    #for i in nlist:

# verify it's big-O
for n in range(10000,100000,10000):
    start = time.time()
    findnum(n, 2)
    end = time.time()
    print("size: %d time %f" % (n, end-start))