# ASABEL
# build a carbon fixation space and look for specific pathways

# input in command line as: mod -f all_pathways_expansion.py

###############################
## import functions
include("utils/functions_co2_01.py")

## import grammar scripts
include("grammars/all_grammar_2.py")



###############################
## define stragety

## predicates
# only one SCoA per molecule
# expand to no more than 6 C atoms
strat = (
    addUniverse(helpermols)
    >> addSubset(eductmols)
    >> rightPredicate[
        lambda d: all(g.vLabelCount("CoA") <= 1 for g in d.right)
    ](
        rightPredicate[
        lambda d: all(g.vLabelCount("C") <= 6 for g in d.right)
    ](repeat[4](rset)))
)



###############################

## define label settings
ls = LabelSettings(LabelType.Term, LabelRelation.Unification)

## calculate hypergraph
dg = DG(graphDatabase = eductmols, labelSettings = ls)
dg.build().execute(strat)


###############################

## print dg
# hide cofactors and helpermolecules
dgprint = hide_mols(helpermols)


dg.print(dgprint)


###############################
## save the dg as a dump
dgname = "all_pathways_grammar_2"
dg.dump("dg_dump/" + dgname + ".dg")

display_size_dg(dg)

