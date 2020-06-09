"""
BNsimpleReduction
Created on Mon Jun 8 2020
Code author : Chun-Kyung Lee(Korea Advanced Institute of Science and Technology)
Contact: chunkyung@kaist.ac.kr
"""

import BNSimpleReduction as BNred

# The first parameter is the name of the network file in the networks directory.
# The second parameter is the desired attractor of the network. The node order must match that of the network file.
# See the github repository for more details (https://github.com/choonlog/BNSimpleReduction).
# 00110010110000000000100001001011
BNred.main("./networks/metastasis_influence_network.txt", "00110010110000000000100001001011")