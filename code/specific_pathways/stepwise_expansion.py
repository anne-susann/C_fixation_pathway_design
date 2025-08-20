# ASABEL
# build any pathway step by step

###############################

## import grammar script
include("grammars/all_grammar_2.py")
include("utils/functions_co2_01.py")

print(rset)

rule_56 = ruleGML('rules/GLYOX_mutase_ala_01.gml') 
rule_57 = ruleGML('rules/GLYOX_transaminase_01.gml')
rule_58 = ruleGML('rules/GLYOX_transaminase_02.gml')
rule_59 = ruleGML('rules/GLYOX_transferase_carboxy_malCoA_01.gml')


rset.append(rule_56)
rset.append(rule_57)
rset.append(rule_58)
rset.append(rule_59)

print(rset)

balanine    = smiles("C(CN)C(=O)O", "beta-ALANINE")
Lalanine    = smiles("CC(C(=O)O)N", "L-ALANINE")

eductmols.append(balanine)
eductmols.append(Lalanine)

# rule_glyox = ruleGML("rules/GLYOX_lysis_isocit_01.gml")
# rset.append(rule_glyox)
# print(rset)

## expanstion strategy for stepwise expansion
# define that a rule is only applied to the specified educt and gives the specified product
# using only specified rule
def educt_product(univ, educt, product, rule):
    return (addUniverse(univ)
                >> addSubset(educt) 
                >> leftPredicate[lambda d: educt in d.left](
                    rightPredicate[lambda d: product in d.right](rule)
                )
            )

## define strategy 
# Bar Even PNAS (4 step pathway + glyoxylate)
# strat = (
#         educt_product(helpermols, succ, succCoA, rule_01)
#     >> educt_product(helpermols, succCoA, ketogl, rule_10)    
#     >> educt_product(helpermols, ketogl, isocit, rule_11)
#     >> educt_product(helpermols, isocit, succ, rule_53) 
#     >> educt_product(helpermols, acCoA, malylCoA, rule_54)
#     >> educt_product(helpermols, malylCoA, malate, rule_36)
# )

# Bar Even PNAS (C4-Glyoxylate/ alanine option)
strat = (
        educt_product(helpermols, pyruv, pep, rule_15)    
    >> educt_product(helpermols, pep, oxala, rule_13)
    >> educt_product(helpermols, oxala, malate, rule_03) 
    >> educt_product(helpermols, malate, malylCoA, rule_32)
    >> educt_product(helpermols, malylCoA, glyxo, rule_02)
    >> educt_product(helpermols, acCoA, malCoA, rule_59)
    >> educt_product(helpermols, malCoA, malald, rule_23)
    >> educt_product(helpermols, Lalanine, balanine, rule_57)
    >> educt_product(helpermols, balanine, Lalanine, rule_56)
    >> educt_product(helpermols, Lalanine, pyruv, rule_57)

    # >> educt_product(helpermols, malald, HP3, rule_24)
    # >> educt_product(helpermols, HP3CoA, acryCoA, rule_22)
)

# Bar Even 2012 J. Exp. Bot. (6 step pathway b) )
# strat = (
#         educt_product(helpermols, acCoA, pyruv, rule_10)
#     >> educt_product(helpermols, pyruv, pep, rule_15)    
#     >> educt_product(helpermols, pep, oxala, rule_13)
#     >> educt_product(helpermols, oxala, malate, rule_03) 
#     >> educt_product(helpermols, malate, malylCoA, rule_32)
#     >> educt_product(helpermols, malylCoA, glyxo, rule_02)
# )

# Bar Even 2012 J. Exp. Bot. (6 step pathway c) )
# strat = (
#         educt_product(helpermols, oxala, malate, rule_03) 
#     >> educt_product(helpermols, malate, malylCoA, rule_32)
#     >> educt_product(helpermols, malylCoA, glyxo, rule_02)
#     >> educt_product(helpermols, succ, isocit, rule_55)
#     >> educt_product(helpermols, isocit, aconi, rule_07)
#     >> educt_product(helpermols, aconi, citrate, rule_09)    
#     >> educt_product(helpermols, citrate, citCoA, rule_01)
#     >> educt_product(helpermols, citCoA, oxala, rule_02)
# )


## define label settings
ls = LabelSettings(LabelType.Term, LabelRelation.Unification)

## calculate hypergraph
dg = DG(graphDatabase = inputGraphs, labelSettings = ls)
dg.build().execute(strat)

## flow query
# include("strategies/3HP4HB_flowq_2.py")


## print dg
# hide cofactors and helpermolecules
# dgprint = hide_mols(HPHB_helpermols)
# dg.print(dgprint)

# print_input_rules()
dg.print()

## save the dg as a dump
dgname = "stepwise_" + "bar_even_PNAS_glyox_ala"
dg.dump("dg_dump/" + dgname + ".dg")

###############################
## petri Net
# include("strategies/petriNet.py")