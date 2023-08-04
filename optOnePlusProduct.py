"""
BNsimpleReduction
Created on Mon Jun 8 2020
Code author : Chun-Kyung Lee(Korea Advanced Institute of Science and Technology)
Contact: chunkyung@kaist.ac.kr
"""

import re
from tqdm import tqdm

# Non-recursive depth first search algorithm
def DFS(graph, start_vertex, onlyOnePlusProduct):
    visited = set()
    traversal = []
    stack = [start_vertex]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            traversal.append(vertex)
            if vertex in onlyOnePlusProduct:
                try:
                    stack.extend(reversed(graph[vertex]))   # add vertex in the same order as visited
                except:
                    pass
    return traversal

def main(allPlusProduct):
    allPlusProduct = allPlusProduct.strip()
    allPlusProductLine = allPlusProduct.splitlines()

    onlyOnePlusProduct = []
    multiPlusProducts = []
    selfFeedbackNode = []
    graph = {}
    multiPlusProductDic = {}
    allPlusProductDic = {}
    for line in allPlusProductLine:
        lineSplit = line.split("=")
        outputNode = lineSplit[0].strip()
        inputNode = lineSplit[1].strip()

        allPlusProductDic[outputNode] = inputNode

        inputNodeSplit = inputNode.split(" | ")
        if len(inputNodeSplit) == 1:
            if not outputNode in inputNode:
                # Only one plus product
                onlyOnePlusProduct.append(outputNode)
            else:
                # multi plus products
                selfFeedbackNode.append(outputNode)
        else:
            multiPlusProducts.append(outputNode)
            multiPlusProductDic[outputNode] = inputNode

        # Extract nodes from each logic expression and create one list
        inputNodeList = re.findall(r'\w+', inputNode)

        # Remove duplicates in list
        inputNodeList = [x for i, x in enumerate(inputNodeList) if i == inputNodeList.index(x)]

        # Set the input of DFS function
        graph[outputNode] = inputNodeList

    multiPlusProductDicRaw = multiPlusProductDic.copy()

    for multiPlusProduct in multiPlusProducts:
        for multiPlusProductInput in graph[multiPlusProduct]:
            # Call DFS function
            if multiPlusProduct in DFS(graph, multiPlusProductInput, onlyOnePlusProduct):
                multiPlusProductDic[multiPlusProduct] = multiPlusProductDic[multiPlusProduct].replace(multiPlusProductInput, "1")
            else:
                multiPlusProductDic[multiPlusProduct] = multiPlusProductDic[multiPlusProduct].replace(multiPlusProductInput, "0")

        termList = multiPlusProductDicRaw[multiPlusProduct].split(" | ")
        scoreList = multiPlusProductDic[multiPlusProduct].split(" | ")
        scoreDic = {}
        for term, score in zip(termList, scoreList):
            score = score.replace("&", "+")
            score = eval(score)
            scoreDic[term] = score

        # Find minimum value in dictionary
        result = min(scoreDic.items(), key=lambda k: k[1])
        allPlusProductDic[multiPlusProduct] = list(result)[0]

    formatTransform = ""
    formatFVS = ""
    for node in allPlusProductDic:
        BooleanExpression = node + " = " + allPlusProductDic[node]
        formatTransform += BooleanExpression + "\n"

        BooleanExpressionList = re.findall(r'\w+', BooleanExpression)
        BooleanExpressionListOutput = BooleanExpressionList[0]
        BooleanExpressionListInput = BooleanExpressionList[1:]

        # Remove duplicates in list
        BooleanExpressionListInput = [x for i, x in enumerate(BooleanExpressionListInput) if i == BooleanExpressionListInput.index(x)]

        for v in BooleanExpressionListInput:
            formatFVS += BooleanExpressionListOutput + ", " + v + "\n"

    return formatTransform, formatFVS

# e.g.,
# allPlusProduct = '''
# x01 = x04 & x06
# x02 = x05 & x06
# x03 = x01
# x04 = x01 | x03
# x05 = (x02 & x04) | (x03 & x04)
# x06 = x05 & x06
# '''
# main(allPlusProduct)
