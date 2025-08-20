# ASABEL
# build 3HP4HB cycle step by step using established rules

# input in command line as: mod -e "params=[p0]" -f 3HP4HB_stepwise_expansion.py
# p0 = grammar_ver

###############################

## set parameters
grammar_ver = str(params[0])

## import grammar script
include("grammars/3HP4HB_grammar_"+grammar_ver+".py")
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
        educt_product(HPHB_helpermols, succCoA, succald, red_reduc_)
    >> educt_product(HPHB_helpermols, succald, HB4, red_dehydr_)    
    >> educt_product(HPHB_helpermols, HB4, HB4CoA, activ_synth_)
    >> educt_product(HPHB_helpermols, HB4CoA, crotCoA, dehydr_4HB)
    >> educt_product(HPHB_helpermols, crotCoA, HB3CoA, rehydr_crot)
    >> educt_product(HPHB_helpermols, HB3CoA, acacetCoA, oxi_dehydr_)
    >> educt_product(HPHB_helpermols, acacetCoA, acCoA, activ_trans_)
    >> educt_product(HPHB_helpermols, acCoA, malCoA, carb_)
    >> educt_product(HPHB_helpermols, malCoA, malald, red_reduc_)
    >> educt_product(HPHB_helpermols, malald, HP3, red_dehydr_)
    >> educt_product(HPHB_helpermols, HP3, HP3CoA, activ_synth_)
    >> educt_product(HPHB_helpermols, HP3CoA, acryCoA, dehydr_3HP)
    >> educt_product(HPHB_helpermols, acryCoA, propCoA, red_reduc_acc)
    >> educt_product(HPHB_helpermols, propCoA, metmalCoA, carb_)
    >> educt_product(HPHB_helpermols, metmalCoA, succCoA, rearr_mutase)    
)

## define label settings
ls = LabelSettings(LabelType.Term, LabelRelation.Unification)

## calculate hypergraph
dg = DG(graphDatabase = inputGraphs, labelSettings = ls)
dg.build().execute(strat)

## flow query
# include("strategies/3HP4HB_flowq_2.py")


## print dg
# hide cofactors and helpermolecules
dgprint = hide_mols(HPHB_helpermols)
dg.print(dgprint)

## save the dg as a dump
dgname = "3HP4HB_stepwise_" + grammar_ver
dg.dump("dg_dump/" + dgname + ".dg")

###############################
## petri Net
# include("strategies/petriNet.py")