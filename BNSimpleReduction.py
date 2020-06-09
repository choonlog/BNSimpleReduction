"""
BNsimpleReduction
Created on Mon Jun 8 2020
Code author : Chun-Kyung Lee(Korea Advanced Institute of Science and Technology)
Contact: chunkyung@kaist.ac.kr
"""

import allPlusProducts
import os
import shutil
import optOnePlusProduct
import time

def main(path, desiredAttr):
    startTime = time.time()
    fileNameNoEx = os.path.splitext(os.path.basename(path))[0]

    with open(path) as file:
        formatNormal = file.read().strip()

    # Get the all plus products network
    formatTransformAllPlus, formatFVS_traAllPlus, formatFVS_ori = allPlusProducts.main(formatNormal, desiredAttr)

    # Get the all one products network
    formatTransformOptOnePlus, formatFVS_traOptOnePlus = optOnePlusProduct.main(formatTransformAllPlus)

    outputDir = "./results/" + fileNameNoEx + "_" + str(desiredAttr)

    if os.path.exists(outputDir):
        shutil.rmtree(outputDir)
    os.makedirs(outputDir)

    with open(outputDir + "/AllPlusProductsNet.txt", "w") as text_file:
        text_file.write(formatTransformAllPlus.strip())

    with open(outputDir + "/AllPlusProductsNet_forFVSFINDER.txt", "w") as text_file:
        text_file.write(formatFVS_traAllPlus.strip())

    with open(outputDir + "/OnePlusProductNet.txt", "w") as text_file:
        text_file.write(formatTransformOptOnePlus.strip())

    with open(outputDir + "/OnePlusProductsNet_forFVSFINDER.txt", "w") as text_file:
        text_file.write(formatFVS_traOptOnePlus.strip())

    print(".txt files with the reduced network is saved.")
    print("Total time for reducing the network: " + str(time.time() - startTime) + " sec")
    print("Complete!")