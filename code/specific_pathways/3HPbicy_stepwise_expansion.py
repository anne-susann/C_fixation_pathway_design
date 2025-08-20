# ASABEL
# build 3HP bicycle step by step using established rules

# input in command line as: mod -e "params=[p0]" -f 3HPbicy_stepwise_expansion.py
# p0 = grammar_ver

###############################

## set parameters
grammar_ver = str(params[0])

## import grammar script
include("grammars/3HPbicy_grammar_"+grammar_ver+".py")
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
        # 2 rule version
        educt_product( HP3bicy_helpermols, succCoA, succ, activ_trans_succCoA)
    >> educt_product( HP3bicy_helpermols, succ, fumarate, oxi_dehydr_succ)
    >> educt_product( HP3bicy_helpermols, fumarate, malate, rehydr_malate)
        # 2 rule version
    >> educt_product( HP3bicy_helpermols, malate, malylCoA, activ_trans_malCoA)
    >> educt_product( HP3bicy_helpermols, malylCoA, glyxo, activ_lysis_)
    >> educt_product( HP3bicy_helpermols, propCoA, metmalylCoA, activ_lysis_rev)
    >> educt_product( HP3bicy_helpermols, metmalylCoA, mesaC1CoA, dehydr_)
    >> educt_product( HP3bicy_helpermols, mesaC1CoA, mesaC4CoA, rearr_trans_mesa)
    >> educt_product( HP3bicy_helpermols, mesaC4CoA, citmalCoA, rehydr_mesa)
    >> educt_product( HP3bicy_helpermols, citmalCoA, pyruv, activ_lysis_)
    >> educt_product( HP3bicy_helpermols, acCoA, malCoA, carb_)
    >> educt_product( HP3bicy_helpermols, malCoA, malald, red_reduc_)
    >> educt_product( HP3bicy_helpermols, malald, HP3, red_dehydr_)
    >> educt_product( HP3bicy_helpermols, HP3, HP3CoA, activ_synth_)
    >> educt_product( HP3bicy_helpermols, HP3CoA, acryCoA, dehydr_)
    >> educt_product( HP3bicy_helpermols, acryCoA, propCoA, red_reduc_acc)
    >> educt_product( HP3bicy_helpermols, propCoA, metmalCoA, carb_)
    >> educt_product( HP3bicy_helpermols, metmalCoA, succCoA, rearr_mutase)
    # >> educt_product(HP3bicy_helpermols, succCoA, succ, activ_trans_CoA)    
)

## define label settings
ls = LabelSettings(LabelType.Term, LabelRelation.Unification)

## calculate hypergraph
dg = DG(graphDatabase = HP3bicy_eductmols, labelSettings = ls)
dg.build().execute(strat)

## flow query
# include("strategies/3HPbicy_flowq_1.py")


## print dg
# hide cofactors and helpermolecules
dgprint = hide_mols(HP3bicy_helpermols)
dg.print(dgprint)
# dg.print()

## save the dg as a dump
dgname = "3HPbicy_stepwise_" + grammar_ver
dg.dump("dg_dump/" + dgname + ".dg")

###############################
## petri Net
# include("strategies/petriNet.py")