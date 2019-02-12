#Given a list of numbers in random order, 
# write an algorithm that works in O(nlog(n)) to find the kth smallest number in the list.
import time
import random
def findnum (n, k):
    nlist = [random.randrange(10000) for x in range(n)] 
    nlist.sort()
#    print(nlist)
    print(nlist[k])

# findnum(100, 2)

def findnum1 (n, k):
    nlist = [random.randrange(10000) for x in range(n)] 
    for i in nlist:
        

for n in range(100,1000,100):
    start = time.time()
    findnum(n, 2)
    end = time.time()
    print("size: %d time %f" % (n, end-start))