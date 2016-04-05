import sys
filename = sys.argv[1]
kT = sys.argv[2]
k = int(float(kT))
edgesList = []
with open(filename) as f:
    for line in f:
        tmp=line.split()
        a=tmp[0]
        b=tmp[1]
        aN = int(float(a))
        bN = int(float(b))
        edgesList.append([aN, bN])
f.close()
#print(edgesList)
tmpList = []
for item in edgesList:
    tmpList.append(item[0])
    tmpList.append(item[1])
nodesList = []
nodesList = list(set(tmpList))
#print(nodesList)


#######################################
def neighbours(num):
    myListTmp = []
    for i in edgesList:
        if num in i:
            if num == i[0]:
                myListTmp.append(i[1])
            elif num == i[1]:
                myListTmp.append(i[0])
    return myListTmp
#######################################


#######################################
def intersection(myListAnI, myListBnI):
    myListTmp = []
    myListTmp = list(set(myListAnI) & set(myListBnI))
    return myListTmp
#######################################


#######################################
def size(myListS):
    return len(myListS)
#######################################


###############################
#################################
#######################################

def crummy_code_to_reduce_graph_to_k_truss(myList, k):
    #print(nodesList)
    for i in myList:
        a = i[0]
        b = i[1]
        sizeP = size(intersection(neighbours(a), neighbours(b)))        
        if  sizeP < (k - 2):
            myList.remove(i)
    listDict = {}
    for n in nodesList:
        listDict[n] = neighbours(n)
    return listDict

#######################################


graph = crummy_code_to_reduce_graph_to_k_truss(edgesList, k)
path = []

def find(n,z,cycle):
    for l in graph[n]:
        if l == z:
            return cycle
        elif l not in path:
            cycle.append(l)
            path.append(l)
            find(l,z,cycle)
        else:
            break

for z in nodesList:
    path = []
    for n in graph[z]:
        cycle = []
        cycle.append(n)
        path.append(n)
        find(n,z,cycle)
    if size(cycle)>=k:
        print(cycle)
