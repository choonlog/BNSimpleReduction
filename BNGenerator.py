"""
BNsimpleReduction
Created on Mon Jun 8 2020
Code author : Chun-Kyung Lee(Korea Advanced Institute of Science and Technology)
Contact: chunkyung@kaist.ac.kr
"""

import random
import pickle

def avg(lst):
    return sum(lst) / len(lst)

def generator(nodeNum):
    totalLogicDic = pickle.load(open("./data/totalLogic.p", "rb"))

    allNodeLength = nodeNum

    # Set the minimum indegree in the graph
    minIndegree = 1

    # Set the maximum indegree in the graph
    maxIndegree = 3
    fillNumber = len(str(allNodeLength))
    allNodes = ["x" + str(i).zfill(fillNumber) for i in range(1, allNodeLength + 1)]
    formatNormal = ""
    indegreeList = []

    for node in allNodes:

        # Random selection in discrete uniform distribution between minimum and maximum values
        selectedNodes = random.sample(allNodes, random.randint(minIndegree, maxIndegree))
        selectedNodesLen = len(selectedNodes)
        indegreeList.append(selectedNodesLen)
        # Random selection in Biological Boolean expressions
        biologicalRandomLogic = random.choice(totalLogicDic[str(selectedNodesLen)])

        for n, selectNode in enumerate(selectedNodes):
            existingNode = "z" + str(n + 1).zfill(2)
            biologicalRandomLogic = biologicalRandomLogic.replace(existingNode, selectNode)

        biologicalRandomLogic = biologicalRandomLogic.replace("&", "and").replace("|", "or").replace("~", "not ")
        formatNormal = formatNormal + node + " = " + biologicalRandomLogic + "\n"

    return formatNormal

formatNormal = generator(20)
netName = "RBN_1"
with open(netName + ".txt", "w") as text_file:
    text_file.write(formatNormal)