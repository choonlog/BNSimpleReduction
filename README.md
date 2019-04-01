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
AKT1 = CTNNB1 and (NICD or TGFbeta or GF_ or CDH2) and not p53 and not miR34 and not CDH1
AKT2 = TWIST1 and (TGFbeta or GF_ or CDH2) and not (miR203 or miR34 or p53)
Apoptosis = (p53 or p63 or p73 or miR200 or miR34) and not ZEB2 and not AKT1 and not ERK
CDH1 = not TWIST1 and not SNAI2 and not ZEB1 and not ZEB2 and not SNAI1 and not AKT2
CDH2 = TWIST1
CTNNB1 = not DKK1 and not p53 and not AKT1 and not miR34 and not miR200 and not CDH1 and not CDH2 and not p63
CellCycleArrest = (miR203 or miR200 or miR34 or ZEB2 or p21) and not AKT1
DKK1 = CTNNB1 or NICD
DNAdamage = _INPUT_
ECM = _INPUT_
EMT = CDH2 and not CDH1
ERK = (SMAD or CDH2 or GF_ or NICD) and not AKT1
GF_ = not CDH1 and (GF_ or CDH2)
Invasion = (SMAD and CDH2) or CTNNB1
Metastasis = Migration
Migration = VIM and AKT2 and ERK and not miR200 and not AKT1 and EMT and Invasion and not p63
NICD = not p53 and not p63 and not p73 and not miR200 and not miR34 and ECM
SMAD = TGFbeta and not miR200 and not miR203
SNAI1 = (NICD or TWIST1) and not miR203 and not miR34 and not p53 and not CTNNB1
SNAI2 = (TWIST1 or CTNNB1 or NICD) and not miR200 and not p53 and not miR203
TGFbeta = (ECM or NICD) and not CTNNB1
TWIST1 = CTNNB1 or NICD or SNAI1
VIM = CTNNB1 or ZEB2
ZEB1 = ((TWIST1 and SNAI1) or CTNNB1 or SNAI2 or NICD) and not miR200
ZEB2 = (SNAI1 or (SNAI2 and TWIST1) or NICD) and not miR200 and not miR203
miR200 = (p63 or p53 or p73) and not (AKT2 or SNAI1 or SNAI2 or ZEB1 or ZEB2)
miR203 = p53 and not (SNAI1 or ZEB1 or ZEB2)
miR34 = not (SNAI1 or ZEB1 or ZEB2) and (p53 or p73) and AKT2 and not p63 and not AKT1
p21 = ((SMAD and NICD) or p63 or p53 or p73 or AKT2) and not (AKT1 or ERK)
p53 = (DNAdamage or CTNNB1 or NICD or miR34) and not SNAI2 and not p73 and not AKT1 and not AKT2
p63 = DNAdamage and not NICD and not AKT1 and not AKT2 and not p53 and not miR203
p73 = DNAdamage and not p53 and not ZEB1 and not AKT1 and not AKT2
```

You should write '_INPUT_' for the Boolean transfer function of all input nodes with the indegree of 0 like DNAdamage and ECM in the example above.
