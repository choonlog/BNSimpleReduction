<img src="BNSimpleReduction.png" alt="BNSimpleReduction" />

# BNSimpleReduction
BNSimpleReduction is a Python package that reduces Boolean networks in such a way that only one product term having literals with no negation is maintained. Thanks to the network reduction by BNSimpleReduction, the minimum FVS found with respect to the reduced network can be applied to the original network, thus enabling efficient control in terms of the number of control inputs. A related paper has been recently published(https://ieeexplore.ieee.org/document/9273230?source=authoralert).

## Installation
You can simply download BNSimpleReduction from this git repository, while setup.py is not provided. BNSimpleReduction is executed on any operating system (Windows, Mac OS, Linux, etc), but Python 3.5 or higher versions must be installed to run the program. The following package can be used to derive the minimum FVS after running BNSimpleReduction.
* https://github.com/needleworm/fvs

## Output
1. AllPlusProductsNet.txt: Reduced network consisting of all plus products
2. OnePlusProductNet.txt: Reduced network consisting of One plus product
3. AllPlusProductsNet_forFVSFINDER.txt: FVS FINDER input format of the reduced network consisting of all plus products
4. OnePlusProductsNet_forFVSFINDER.txt: FVS FINDER input format of the reduced network consisting of one plus products

## Example
<img src="animation.gif" alt="BNSimpleReduction" />

The following function is in main.py:
```
import BNSimpleReduction as BNred

# BNred.main(Parameter_1, Parameter_2)
# Parameter_1: Boolean network file
# Parameter_2: Desired fixed point attractor (steady state) in the network
BNred.main("./networks/metastasis_influence_network.txt", "00110010110000000000100001001011")
```

The first parameter is the name of the network file in the networks directory. The second parameter is the desired attractor of the network. The node order must match that of the network file. Boolean logic in the network file should be written as follows.
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

You should write '\_INPUT\_' for all input nodes with the indegree of 0 like DNAdamage and ECM in the example above.

# BNGenerator
BNGenerator is executed independently of BNSimpleReduction, and is a software that generates a random Boolean network using Biological Boolean logics extracted from 78 Biological Boolean networks in the Cell Collective (https://cellcollective.org/).

## Example
It can be executed by entering the parameters of the generator function in line 44 of BNGenerator.py.
The result is saved in the name specified by the user in line 46.

```
# generator(Parameter_1, Parameter_2, Parameter_3)
# Parameter_1: The number of nodes in the network to be generated
# Parameter_2: Minimum indegree
# Parameter_3: Maximum indegree
formatNormal = generator(20, 1, 3)

netName = "RBN_1"
with open(netName + ".txt", "w") as text_file:
    text_file.write(formatNormal)
```

The number of nodes in the network to be generated is determined by Parameter_1, and the input link of each node is randomly selected from the uniform distribution with a range between Parameter_2 and Parameter_3. Boolean logic is randomly assigned from the Biological Boolean logic collection data (./data/totalLogic.p) according to the indegree after the input link of each node is determined.
