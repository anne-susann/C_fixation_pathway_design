# ASABEL
# test script for rTCA rewrite rules
# GOAL: build rTCA pathway as rewrite rules

# 1. Test: synthetase_01.gml
# 2. Test: lysis_01.gml
# 3. Test: dehydrogenase_01.gml
# 4. Test: 3HB_dehydrogeanse_01.gml
# 5. Test: dehydration_01.gml
# 6. Test: dehydration_02.gml

###############################
# set up grammar 

### molecules

## starter molecules 
## rTCA
oxala       = smiles("C(C(=O)C(=O)O)C(=O)O", "OXALACETIC ACID")
malate      = smiles("C(C(C(=O)O)O)C(=O)O", "MALIC ACID")
fumarate    = smiles("C(=CC(=O)O)C(=O)O", "FUMARIC ACID")
succ        = smiles("OC(=O)CCC(=O)O", "SUCCINIC ACID")
succCoA     = smiles("OC(=O)CCC(=O)S[CoA]", "SUCCINYL COA", allowAbstract = True)
# ketogl      = smiles("C(CC(=O)O)C(=O)C(=O)O", "2-KETOGLUTARIC ACID")
isocit      = smiles("C(C(C(C(=O)O)O)C(=O)O)C(=O)O", "ISOCITRIC ACID")
aconi       = smiles("C(C(=CC(=O)O)C(=O)O)C(=O)O", "ACONITIC ACID")
citrate     = smiles("C(C(=O)O)C(CC(=O)O)(C(=O)O)O", "CITRIC ACID")
# AcCoA       = smiles("CC(=O)S[CoA]", "ACETYL COA", allowAbstract = True)
pyruv       = smiles("CC(=O)C(=O)O", "PYRUVATE")
pep         = smiles("C=C(C(=O)O)OP(=O)(O)O", "PEP")

## other pathways
citCoA      = smiles("C(C(=O)O)C(CC(=O)S[CoA])(C(=O)O)O", "CITRYL COA", allowAbstract = True)
# HP          = smiles("C(CO)C(=O)O", "3HP")
# malald      = smiles("OC(=O)CC=O", "MALONATE SEMIALDEHYDE")
# succald     = smiles("O=CCCC(=O)O", "SUCCINATE SEMIALDEHYDE")

## helper molecules
CoA = graphDFS("[CoA][S][H]")
# ATP = graphDFS("[ADP][Pi]", "ATP")
# ATP = smiles("[AMP][Pi]O[Pi]", "ATP", allowAbstract = True)
# ADP = graphDFS("[ADP]", "ADP")
# AMP = graphDFS("[AMP]", "AMP")
# Pi = graphDFS("[Pi]", "Pi")

ATP       = smiles("[Ad]OP(=O)(O)OP(=O)(O)OP(=O)(O)O", "ATP", allowAbstract = True)
ADP       = smiles("[Ad]OP(=O)(O)OP(=O)(O)O", "ADP", allowAbstract = True)
AMP       = smiles("[Ad]OP(=O)(O)O", "AMP", allowAbstract = True)
Pi        = smiles("OP(=O)(O)O", "Pi")
PPi       = smiles("OP(=O)(O)OP(=O)(O)O", "PPi")



NADPH = graphDFS("[NADP][H]", "NADPH")
NADPplus = graphDFS("[NADP+]", "NADP+")
NADH = graphDFS("[NAD][H]", "NADH")
NADplus = graphDFS("[NAD+]", "NAD+")
hplus = smiles("[H+]", "hplus")
h2o = smiles("O", "H2O")
co2 = smiles("C(=O)=O", "CO2")
hco3 = smiles("C(=O)(O)[O-]", "HCO3-")

## product molecule
#succCoA = smiles("[OC(=O)CCC(=O)][S][CoA]", "SUCCINYL COA")

eductMols = [
            oxala,
            malate,
            fumarate,
            succ,
            succCoA,
            # ketogl,
            # isocit,
            aconi,
            # citrate,
            # AcCoA,
            pyruv,
            pep,
            # citCoA,
            # HP,
            # malald,
            # succald,
            CoA,
            ATP,
            ADP,
            AMP,
            Pi,
            NADPH,
            NADPplus,
            NADH,
            NADplus,
            hplus,
            h2o,
            co2,
            hco3
            ]


### rewrite rules

## all rules of rTCA
# relative path 
# PATH1 = "rules/"
# ## init rule list
# rule_list = []
# # create rule list in the folder
# for file in os.listdir(PATH1):
#     rule_list.append(ruleGML(PATH1 + file))

## for singular rule
rule_list = []
rule_list.append(ruleGML("rules/rTCA_reduction_reductase_01_1.gml"))
rule_list.append(ruleGML("rules/rTCA_reduction_reductase_01_2.gml"))
# rule_list.append(ruleGML("rules/rTCA_dehydration_02.gml"))


###############################
# set up strategy
# define strat
strat = (addSubset(eductMols) >> repeat[4](inputRules))

# define label class settings to term rewrite
ls = LabelSettings(LabelType.Term, LabelRelation.Unification)

## generate derivation graph using the defined strategy
dg = DG(graphDatabase = eductMols, labelSettings = ls)
dg.build().execute(strat)

###############################
# print results
# print derivation graph
dg.print()

# print input rules
for r in inputRules:
    p = GraphPrinter()
    p.setReactionDefault()
    p.withIndex = True
    r.print(p)

# print input mols
for m in eductMols:
    m.print()