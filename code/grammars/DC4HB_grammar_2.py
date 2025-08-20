# ASABEL
# define space for the DC4HB (molecules, cofactors)

### molecules ###############################

## starter molecules
## DC4HB
succCoA     = smiles("OC(=O)CCC(=O)S[CoA]", "SUCCINYL COA", allowAbstract = True)
succald     = smiles("O=CCCC(=O)O", "SUCCINATE SEMIALDEHYDE")
HB4         = smiles("C(CC(=O)O)CO", "4HB")
HB4CoA      = smiles("C(CC(=O)S[CoA])CO", "4-HYDROXYBUTYRYL COA", allowAbstract = True)
crotCoA     = smiles("CC=CC(=O)S[CoA]", "CROTONYL-COA", allowAbstract = True)
HB3CoA      = smiles("CC(CC(=O)S[CoA])O", "3-HYDROXYBUTYRYL COA", allowAbstract = True)
acacetCoA   = smiles("CC(=O)CC(=O)S[CoA]", "ACETOACETYL COA", allowAbstract = True)
acCoA       = smiles("CC(=O)S[CoA]", "ACETYL COA", allowAbstract = True)
pyruv       = smiles("CC(=O)C(=O)O", "PYRUVATE")
pep         = smiles("C=C(C(=O)O)OP(=O)(O)O", "PEP")
oxala       = smiles("C(C(=O)C(=O)O)C(=O)O", "OXALACETIC ACID")
malate      = smiles("C(C(C(=O)O)O)C(=O)O", "MALIC ACID")
fumarate    = smiles("C(=CC(=O)O)C(=O)O", "FUMARIC ACID")
succ        = smiles("OC(=O)CCC(=O)O", "SUCCINIC ACID")

DC4HB_eductmols = [
        succCoA,
        succald,
        HB4,
        HB4CoA,
        crotCoA,
        HB3CoA,
        acacetCoA,
        acCoA,
        pyruv,
        pep,
        oxala,
        malate,
        fumarate,
        succ
        ]

## helper molecules
CoA       = graphDFS("[CoA][S][H]", "CoASH")
ATP       = smiles("[Ad]OP(=O)(O)OP(=O)(O)OP(=O)(O)O", "ATP", allowAbstract = True)
ADP       = smiles("[Ad]OP(=O)(O)OP(=O)(O)O", "ADP", allowAbstract = True)
AMP       = smiles("[Ad]OP(=O)(O)O", "AMP", allowAbstract = True)
Pi        = smiles("OP(=O)(O)O", "Pi")
PPi       = smiles("OP(=O)(O)OP(=O)(O)O", "PPi")
NADPH     = graphDFS("[NADP][H]", "NADPH")
NADPplus  = graphDFS("[NADP+]", "NADP+")
NADH      = graphDFS("[NAD][H]", "NADH")
NADplus   = graphDFS("[NAD+]", "NAD+")
hplus     = smiles("[H+]", "hplus")
h2o       = smiles("O", "H2O")
hco3      = smiles("C(=O)(O)[O-]", "HCO3-")
co2       = smiles("C(=O)=O", "CO2")
Fdred     = graphDFS("[Fdred]", "Fdred")
Fdox      = graphDFS("[Fdox]", "Fdox")


DC4HB_helpermols = [
        CoA,
        ATP,
        ADP,
        AMP,
        Pi,
        PPi,
        NADPH,
        NADPplus,
        NADH,
        NADplus,
        hplus,
        h2o,
        hco3,
        co2,
        Fdred,
        Fdox
        ]

### rules ###############################
# reaction 1
red_reduc_3HP4HB = ruleGML("../rules/3HP4HB_reduction_reductase_succCoA_01.gml")

# reaction 2
red_dehydr_3HP4HB = ruleGML("../rules/3HP4HB_reduction_dehydrogenase_01.gml")

# reaction 3
activ_synth_3HP4HB = ruleGML("../rules/3HP4HB_activation_synthetase_01.gml")

# reaction 4
dehydr_4HB_3HP4HB = ruleGML("../rules/3HP4HB_dehydration_4HBCoA_01.gml")

# reaction 5
rehydr_crot_3HP4HB = ruleGML("../rules/rTCA_dehydration_02_1.gml")

# reaction 6
oxi_dehydr_3HP4HB = ruleGML("../rules/3HP4HB_oxidation_dehydrogenase_3HBCoA_01.gml")

# reaction 7
activ_trans_3HP4HB = ruleGML("../rules/3HP4HB_transferase_acCoA_01_1.gml")

# reaction 8
carb_rTCA = ruleGML("../rules/rTCA_carboxylation_2KFOR_01.gml")

# reaction 9
activ_diki_pep_rTCA = ruleGML("../rules/rTCA_activation_dikinase_01_1.gml")

# reaction 10
carb_pep_rTCA = ruleGML("../rules/rTCA_carboxylation_PEPC_01_1.gml")

# reaction 11
red_dehydr_mal_rTCA = ruleGML("../rules/rTCA_reduction_dehydrogenase_01.gml")

# reaction 12
dehydr_rTCA = ruleGML("../rules/rTCA_dehydration_01.gml")

# reaction 13
red_reduc_fum_rTCA = ruleGML("../rules/rTCA_reduction_reductase_01_2.gml")

# reaction 14
activ_synth_succ_rTCA = ruleGML("../rules/rTCA_activation_synthetase_01.gml")

## define rulesest 

rset_DC4HB = [
        red_reduc_3HP4HB,        # r1   
        red_dehydr_3HP4HB,       # r2   
        activ_synth_3HP4HB,      # r3   
        dehydr_4HB_3HP4HB,       # r4   
        rehydr_crot_3HP4HB,      # r5   
        oxi_dehydr_3HP4HB,       # r6   
        activ_trans_3HP4HB,      # r7   
        carb_rTCA,               # r8       
        activ_diki_pep_rTCA,     # r9       
        carb_pep_rTCA,           # r10
        red_dehydr_mal_rTCA,     # r11       
        dehydr_rTCA,             # r12
        red_reduc_fum_rTCA,      # r13   
        activ_synth_succ_rTCA    # r14       
        ]