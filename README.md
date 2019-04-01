## BNSimpleReduction
BNSimpleReduction is a Python package that reduces Boolean networks using algebraic and structural information. The FVS found in the reduced network can be applied to the original networks, thus enabling efficient control. The paper will soon be published.

## Installation
You can simply download it from this git repository. setup.py is not provided. It does not matter which operating system you use. You need python 3.

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

The first parameter is the name of the network file in the networks folder. The second parameter is the desired attractor of the network. The node order must match the node order of the network file. The third parameter can be True or False. True means leaving only one plus product and False means leaving all plus product when reducing the networks.
