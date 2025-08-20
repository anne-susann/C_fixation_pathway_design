
# ASABEL
# test script for CETCH rewrite rules
# GOAL: build build CETCH pathway as rewrite rules

###############################
# import functions
include("utils/functions_co2_01.py")

# import helpermols
include("grammars/CETCH_grammar_1.py")

# define eductmols
## CETCH
propCoA     = smiles("CCC(=O)S[CoA]", "PROPIONYL COA", allowAbstract = True)
acryCoA     = smiles("C=CC(=O)S[CoA]", "ACRYLYL COA", allowAbstract = True)
# 3HP4HB
metmalCoA   = smiles("CC(C(=O)O)C(=O)S[CoA]", "METHYLMALONYL COA", allowAbstract = True)
succCoA     = smiles("OC(=O)CCC(=O)S[CoA]", "SUCCINYL COA", allowAbstract = True)
succald     = smiles("O=CCCC(=O)O", "SUCCINATE SEMIALDEHYDE")
HB4         = smiles("C(CC(=O)O)CO", "4HB")
HB4CoA      = smiles("C(CC(=O)S[CoA])CO", "4-HYDROXYBUTYRYL COA", allowAbstract = True)
crotCoA     = smiles("CC=CC(=O)S[CoA]", "CROTONYL-COA", allowAbstract = True)
# CETCH
ethmalCoA   = smiles("CCC(C(=O)O)C(=O)S[CoA]", "ETHYLMALONYL COA", allowAbstract = True)
metsuccCoA  = smiles("OC(=O)CC(C)C(=O)S[CoA]", "METHYLSUCCINYL COA", allowAbstract = True)
# reverse 3HP bicy
mesaC1CoA   = smiles("CC(=CC(=O)O)C(=O)S[CoA]", "MESACONYL C1 COA", allowAbstract = True)
metmalylCoA = smiles("CC(C(C(=O)O)O)C(=O)S[CoA]", "METHYLMALYL COA", allowAbstract = True)
glyxo       = smiles("C(=O)C(=O)O", "GLYOXYLATE")
acCoA       = smiles("CC(=O)S[CoA]", "ACETYL COA", allowAbstract = True)
malylCoA    = smiles("C(C(C(=O)O)O)C(=O)S[CoA]", "MALYL COA", allowAbstract = True)
malate      = smiles("C(C(C(=O)O)O)C(=O)O", "MALIC ACID")

eductmols = [
#    propCoA,
#    acryCoA,
#    metmalCoA,
#    succCoA,
#    succald,
#    HB4,
#    HB4CoA,
#    crotCoA,
#    ethmalCoA,
#    metsuccCoA,
#    mesaC1CoA,
#    metmalylCoA,
    glyxo,
    acCoA,
    malylCoA,
    malate
]

###############################
# rule to test
## for singular rule
test_rule_list = []
test_rule_list.append(ruleGML("rules/CETCH_activation_lysis_02.gml"))

###############################
# set up strategy
# define strat
strat = (addUniverse(helpermols) >> 
         addSubset(eductmols) >> repeat[4](test_rule_list))

# define label class settings to term rewrite
ls = LabelSettings(LabelType.Term, LabelRelation.Unification)

## generate derivation graph using the defined strategy
dg = DG(graphDatabase = eductmols, labelSettings = ls)
dg.build().execute(strat)

###############################
# print results
# print derivation graph
dg.print()

"""
## print dg
# hide cofactors and helpermolecules
dgprint = hide_mols(helpermols)
dg.print(dgprint)
"""

# print input rules
for r in inputRules:
    p = GraphPrinter()
    p.setReactionDefault()
    p.withIndex = True
    r.print(p)

# print input mols
for m in eductmols:
    m.print()


# print_all_rules("rules/")
