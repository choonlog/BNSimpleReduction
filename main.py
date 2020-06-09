"""
BNsimpleReduction
Created on Mon Jun 8 2020
Code author : Chun-Kyung Lee(Korea Advanced Institute of Science and Technology)
Contact: chunkyung@kaist.ac.kr
"""

import BNSimpleReduction as BNred

# BNred.main(Parameter_1, Parameter_2)
# Parameter_1: Boolean network file
# Parameter_2: Desired fixed point attractor (steady state) in the network
BNred.main("./networks/metastasis_influence_network.txt", "00110010110000000000100001001011")
