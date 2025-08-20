# ASABEL
# define space for the rTCA (molecules, cofactors)

### molecules ###############################

## starter molecules 
## rTCA
oxala       = smiles("C(C(=O)C(=O)O)C(=O)O", "OXALACETIC ACID")
malate      = smiles("C(C(C(=O)O)O)C(=O)O", "MALIC ACID")
fumarate    = smiles("C(=CC(=O)O)C(=O)O", "FUMARIC ACID")
succ        = smiles("OC(=O)CCC(=O)O", "SUCCINIC ACID")
succCoA     = smiles("OC(=O)CCC(=O)S[CoA]", "SUCCINYL COA", allowAbstract = True)
ketogl      = smiles("C(CC(=O)O)C(=O)C(=O)O", "2-KETOGLUTARIC ACID")
isocit      = smiles("C(C(C(C(=O)O)O)C(=O)O)C(=O)O", "ISOCITRIC ACID")
aconi       = smiles("C(C(=CC(=O)O)C(=O)O)C(=O)O", "ACONITIC ACID")
citrate     = smiles("C(C(=O)O)C(CC(=O)O)(C(=O)O)O", "CITRIC ACID")
citCoA      = smiles("C(C(=O)O)C(CC(=O)S[CoA])(C(=O)O)O", "CITRYL COA", allowAbstract = True)
AcCoA       = smiles("CC(=O)S[CoA]", "ACETYL COA", allowAbstract = True)
pyruv       = smiles("CC(=O)C(=O)O", "PYRUVATE")
pep         = smiles("C=C(C(=O)O)OP(=O)(O)O", "PEP")

## helper molecules
CoA = graphDFS("[CoA][S][H]")
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
Fdred     = graphDFS("[Fdred]", "Fdred")
Fdox      = graphDFS("[Fdox]", "Fdox")

rTCA_eductmols = [
            oxala,
            malate,
            fumarate,
            succ,
            succCoA,
            ketogl,
            isocit,
            aconi,
            citrate,
            citCoA,
            AcCoA,
            pyruv,
            pep
            ]

rTCA_helpermols = [
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
            hco3,
            Fdred,
            Fdox
            ]


### rules ###############################

# define rules
# reaction 1
red_dehydr_mal = ruleGML("../rules/rTCA_reduction_dehydrogenase_01.gml")

# reaction 2 and 7
dehydr_ = ruleGML("../rules/rTCA_dehydration_01.gml")

# reaction 3
red_reduc_fum = ruleGML("../rules/rTCA_reduction_reductase_01_2.gml")

# reaction 4
activ_synth_succ = ruleGML("../rules/rTCA_activation_synthetase_01.gml")

# reaction 5 and 10
carb_ = ruleGML("../rules/rTCA_carboxylation_2KFOR_01.gml")

# reaction 6
carb_iso = ruleGML("../rules/rTCA_carboxylation_IDH_01.gml")

# reaction 8
rehydr_ = ruleGML("../rules/rTCA_dehydration_02_1.gml")

# reaction 9 
activ_lysis_cit = ruleGML("../rules/rTCA_activation_lysis_01.gml")

# reaction 11
activ_diki_pep = ruleGML("../rules/rTCA_activation_dikinase_01_1.gml")

# reaction 12
carb_pep = ruleGML("../rules/rTCA_carboxylation_PEPC_01_1.gml")

# define ruleset

rset_rTCA = [
    red_dehydr_mal,     # r1
    dehydr_,            # r2
    red_reduc_fum,      # r3
    activ_synth_succ,   # r4
    carb_,              # r5
    carb_iso,           # r6
    rehydr_,            # r7
    activ_lysis_cit,    # r8
    activ_diki_pep,     # r9
    carb_pep            # r10
]
