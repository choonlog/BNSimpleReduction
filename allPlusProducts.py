from sympy.logic.boolalg import to_dnf
import re
from tqdm import tqdm

def replaceMultiple(mainString, toBeReplaces, newString):
    # Iterate over the strings to be replaced
    for elem in toBeReplaces:
        # Check if string is in the main string
        if elem in mainString:
            # Replace the string
            mainString = mainString.replace(elem, newString)

    return mainString

def main(modeltext, desiredAttr):

    modeltext = modeltext.strip()

    # Split the modeltext by line
    modeltextLine = modeltext.splitlines()

    # Convert the desiredAttr to dictionary data type
    desiredAttrDic = {}
    s = 0
    for line in modeltextLine:
        IODic = line.split("=")
        desiredAttrDic[IODic[0].strip()] = str(bool(int(desiredAttr[s])))
        s = s + 1

    # Set logic symbols
    and_logic = ["and", "&&"]
    or_logic = ["or", "||"]
    negation_logic = ["not"]

    # Convert each logic expression to disjunctive normal form(DNF)
    formatTransform = ""
    formatFVS_ori = ""
    formatFVS_tra = ""

    for line in tqdm(modeltextLine):

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

        # Remove duplicates in list
        transformedlogicInput = [x for i, x in enumerate(transformedlogicInput) if i == transformedlogicInput.index(x)]

        # Set formatFVS_tra
        for v in transformedlogicInput:
            formatFVS_tra = formatFVS_tra + transformedlogicOutput + ", " + v + "\n"

        # Set formatFVS_ori
        for v in logicInput:
            formatFVS_ori = formatFVS_ori + logicOutput + ", " + v + "\n"

    return formatTransform, formatFVS_tra, formatFVS_ori