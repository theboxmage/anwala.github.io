import math
def printStats(f1, f2):
    f = open(f1, "r")
    o = open(f2, "w+")
    meanC=float(0)
    count=0
    l=[]
    for line in f:
        count += 1
        hold=line.rstrip()
        curr=float(hold.split(",")[1])
        l.append(curr)
        meanC += curr
    l.sort()
    if(len(l) % 2): #Odd
        print("Median: " + str(l[math.floor(len(l)/2)]))
    else: #Even
        i=len(l)/2
        print("Median: " + str((l[int(i)] + l[int(i-1)])/2))
    for x in l:
        o.write(str(x) + "\n")
    o.close()
    mean=meanC/count
    currentSum=0
    for xi in l:
        currentSum += (xi - mean) * (xi - mean)
    stddev = math.sqrt(currentSum / count)
    print("Number of entries: " + str(count))
    print("Mean: ", mean)
    print("Anwala's Friends: " + str(count))
    print("Standard Deviation: " + str(stddev))

printStats("acnwala-friendscount.csv", "NumFriends.txt")
print("\n\n\n\n\n")
printStats("TwitterCount.txt", "NumFriends2.txt")
