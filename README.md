## BNSimpleReduction
BNSimpleReduction is a Python package that reduces Boolean networks using algebraic and structural information. The FVS found in the reduced network can be applied to the original networks, thus enabling efficient control. The paper will soon be published.

## Installation
You can simply download it from this git repository. setup.py is not provided. It does not matter which operating system you use. Only python 3 is supported. The following package should be used to find FVS.
* https://github.com/needleworm/fvs

## Output
- Disjunctive normal form(DNF) of transformed networks
- Reduced networks
- Minimal FVSs of reduced networks
- Minimal FVSs of original networks
- .sif file form for Cytoscape application of reduced networks

## Example
The following function is in main.py:
```
red.LetsReduce("metastasis_influence_network.txt", "00110010110000000000100001001011", True)
```

The first parameter is the name of the network file in the networks folder. The second parameter is the desired attractor of the network. The node order must match the node order of the network file. The third parameter can be True or False. True means leaving only one plus product and False means leaving all plus product when reducing the networks. The network file should be written as follows.
```
x01 = x03 and not x04
x02 = x01 or not x18
x03 = x10 or not x05
x04 = x04 or (x02 and x14)
x05 = (x03 and not x13) or (not x01 and not x13)
x06 = not x20
x07 = not x14 or (x16 and not x10)
x08 = (x04 and not x12) or (x12 and not x04) or (not x04 and not x09)
x09 = (x05 and not x16) or (x16 and not x05)
x10 = x10
x11 = not x08 and not x13
x12 = (x08 and x20) or (not x08 and not x20)
x13 = not x11
x14 = (x16 and x20) or (not x18 and not x20)
x15 = not x08
x16 = (x15 and not x17) or (x17 and not x15)
x17 = x09
x18 = x03
x19 = (x07 and x09) or (x20 and not x07)
x20 = not x09 or not x16
```
