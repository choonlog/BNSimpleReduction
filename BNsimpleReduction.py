"""
BNsimpleReduction
Created on Mon Dec 10 2018
Author: Chun-Kyung Lee(Korea Advanced Institute of Science and Technology)
Contact: chunkyung@kaist.ac.kr
"""
from sympy.logic.boolalg import to_dnf
import re
import datetime
import time
import sys


# Execution time
start_time = time.time()

def LetsReduce(fileNmae, desiredAttr, discardAllTerm=True):
    if fileNmae == "" or desiredAttr == "":
        print("The parameters have not been entered")
        sys.exit()

    path = "./networks/"
    with open(path + fileNmae, 'r') as network:
        modeltext = network.read()
        #print(modeltext)

    # Split the modeltext by line
    modeltextLine = modeltext.splitlines()

    # Convert the desiredAttr to dictionary data type
    desiredAttrDic = {}
    s = 0
    for line in modeltextLine:
        IODic = line.split("=")
        desiredAttrDic[IODic[0].strip()] = str(bool(int(desiredAttr[s])))
        s = s + 1

    #print(desiredAttrDic)

    # Function for multiple string replacement at a time
    def replaceMultiple(mainString, toBeReplaces, newString):
        # Iterate over the strings to be replaced
        for elem in toBeReplaces:
            # Check if string is in the main string
            if elem in mainString:
                # Replace the string
                mainString = mainString.replace(elem, newString)

        return mainString

    # Set logic symbols
    and_logic = ["and", "&&"]
    or_logic = ["or", "||"]
    negation_logic = ["not"]

    # Convert each logic expression to disjunctive normal form(DNF)
    final_list = []
    formatExpressionDnf = "--------------- Original logic formatted to sum of products ---------------\n"
    formatTransform = "------------------------------ Reduced network ------------------------------\n"
    formatFVS_ori = "----------- Format for feedback vertex sets of the original network ----------\nTarget, Source\n"
    formatFVS_tra = "----------- Format for feedback vertex sets of the reduced network -----------\nTarget, Source\n"
    formatCytoscape= "---------------- Format for cytoscape of the reduced network -----------------\nTarget\tInteraction\tSource\n"

    for line in modeltextLine:

        # Convert given logic symbols to official symbols
        and_rep = replaceMultiple(line, and_logic, "&")
        or_rep = replaceMultiple(and_rep, or_logic, "|")
        negation_rep = replaceMultiple(or_rep, negation_logic, "~")

        str1 = negation_rep.split("=")
        expression = str1[1].strip()

        # Extract nodes from each logic expression and create one list
        logicList = re.findall(r'\w+', negation_rep)

        logicOutput = logicList[0]
        logicInput = logicList[1:]

        # Remove duplicates in list
        logicInput = [x for i, x in enumerate(logicInput) if i == logicInput.index(x)]
        # print(logicOutput, logicInput[0])

        if logicInput[0] == "_INPUT_":
            continue

        for node in logicInput:

            # Input negation
            if desiredAttrDic[node] == "False":
                # Exact replacement using regular expression
                expression = re.sub(r"\b" + node + r"\b", "( ~ " + node + ")", expression)

        # Output negation
        if desiredAttrDic[logicOutput] == "False":
            expression = expression.replace(expression, " ~ ( " + expression + ")")

       # print(expression)
        expressionDnf = to_dnf(expression, True)
       # print(expressionDnf)
        formatExpressionDnf = formatExpressionDnf + str(expressionDnf) + "\n"

        if discardAllTerm:
            # Remain only one plusproduct
            # If the plus product are more than one, select the first one.
            x = str(expressionDnf).split("|")
            for i in x:
                if not ("~") in i:
                    termSelected = i.strip()
                    break

            transformedLogic = logicOutput + " = " + termSelected
            formatTransform = formatTransform + transformedLogic + "\n"

        else:
            # Remain all plusproducts
            plusProductSep = " | "
            x = str(expressionDnf).split("|")
            plusProductList = []
            for i in x:
                if not ("~") in i:
                    plusProductList.append(i.strip())
            termSelected = plusProductSep.join(plusProductList)
            #print(termSelected)
            transformedLogic = logicOutput + " = " + termSelected
            formatTransform = formatTransform + transformedLogic + "\n"

        # Extract nodes from each logic expression and create one list
        transformedlogicList = re.findall(r'\w+', transformedLogic)
        transformedlogicOutput = transformedlogicList[0]
        transformedlogicInput = transformedlogicList[1:]


        # Set formatFVS_tra
        for v in transformedlogicInput:
            formatFVS_tra = formatFVS_tra + transformedlogicOutput + ", " + v + "\n"

        # Set formatFVS_ori
        for v in logicInput:
            formatFVS_ori = formatFVS_ori + logicOutput + ", " + v + "\n"

        # Set formatCytoscape
        logicNodeList = re.findall(r'\w+', transformedLogic)
        outputNode = logicNodeList[0]
        logicNodeList = logicNodeList[1:]

        # 2. formatCytoscape
        # Remove duplicates from randomBinaries
        logicNodeListPure = [x for i, x in enumerate(logicNodeList) if i == logicNodeList.index(x)]
        for v in logicNodeListPure:
            formatCytoscape = formatCytoscape + outputNode + "\tactivation\t" + v + "\n"

    print(formatExpressionDnf)
    print(formatTransform)
    print(formatFVS_tra)
    print(formatFVS_ori)
    print(formatCytoscape)
    print("Execution time: " + str(time.time() - start_time) + " sec")

    nowDate = str(datetime.datetime.now().strftime("%Y%m%d%H%M%S(%A)"))
    with open("./results/" + fileNmae, "w") as text_file:
        text_file.write(nowDate + "\n\n\n" + formatExpressionDnf + "\n\n" + formatTransform + "\n\n" + formatFVS_tra + "\n\n" + formatFVS_ori + "\n\n" + formatCytoscape)