# ASABEL
# build DC4HB cycle step by step using established rules

# input in command line as: mod -e "params=[p0]" -f DC4HB_stepwise_expansion.py
# p0 = grammar_ver

###############################

## set parameters
grammar_ver = str(params[0])

## import grammar script
include("grammars/DC4HB_grammar_"+grammar_ver+".py")
include("utils/functions_co2_01.py")

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
strat = (
        educt_product(DC4HB_helpermols, succCoA, succald, red_reduc_3HP4HB)
    >>educt_product(DC4HB_helpermols, succald, HB4, red_dehydr_3HP4HB)
    >>educt_product(DC4HB_helpermols, HB4, HB4CoA, activ_synth_3HP4HB)
    >>educt_product(DC4HB_helpermols, HB4CoA, crotCoA, dehydr_4HB_3HP4HB)
    >>educt_product(DC4HB_helpermols, crotCoA, HB3CoA, rehydr_crot_3HP4HB)
    >>educt_product(DC4HB_helpermols, HB3CoA, acacetCoA, oxi_dehydr_3HP4HB)
    >>educt_product(DC4HB_helpermols, acacetCoA, acCoA, activ_trans_3HP4HB)
    >>educt_product(DC4HB_helpermols, acCoA, pyruv, carb_rTCA)
    >>educt_product(DC4HB_helpermols, pyruv, pep, activ_diki_pep_rTCA)
    >>educt_product(DC4HB_helpermols, pep, oxala, carb_pep_rTCA)
    >>educt_product(DC4HB_helpermols, oxala, malate, red_dehydr_mal_rTCA)
    >>educt_product(DC4HB_helpermols, malate, fumarate, dehydr_rTCA)
    >>educt_product(DC4HB_helpermols, fumarate, succ,red_reduc_fum_rTCA)
    >>educt_product(DC4HB_helpermols, succ, succCoA,activ_synth_succ_rTCA)
)

## define label settings
ls = LabelSettings(LabelType.Term, LabelRelation.Unification)

## calculate hypergraph
dg = DG(graphDatabase = inputGraphs, labelSettings = ls)
dg.build().execute(strat)

## flow query

## print dg
# hide cofactors and helpermolecules
dgprint = hide_mols(DC4HB_helpermols)
dg.print(dgprint)

## save the dg as a dump
# dgname = "DC4HB_stepwise_" + grammar_ver
# dg.dump("dg_dump/" + dgname + ".dg")

###############################
## petri Net
# include("strategies/petriNet.py")