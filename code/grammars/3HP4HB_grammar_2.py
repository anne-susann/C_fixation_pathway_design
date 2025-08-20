# ASABEL
# define space for the 3HP4HB (molecules, cofactors)

### molecules ###############################

## starter molecules
## 3HP4HB
succCoA     = smiles("OC(=O)CCC(=O)S[CoA]", "SUCCINYL COA", allowAbstract = True)
succald     = smiles("O=CCCC(=O)O", "SUCCINATE SEMIALDEHYDE")
HB4         = smiles("C(CC(=O)O)CO", "4HB")
HB4CoA      = smiles("C(CC(=O)S[CoA])CO", "4-HYDROXYBUTYRYL COA", allowAbstract = True)
crotCoA     = smiles("CC=CC(=O)S[CoA]", "CROTONYL-COA", allowAbstract = True)
HB3CoA      = smiles("CC(CC(=O)S[CoA])O", "3-HYDROXYBUTYRYL COA", allowAbstract = True)
acacetCoA   = smiles("CC(=O)CC(=O)S[CoA]", "ACETOACETYL COA", allowAbstract = True)
acCoA       = smiles("CC(=O)S[CoA]", "ACETYL COA", allowAbstract = True)
malCoA      = smiles("C(C(=O)O)C(=O)S[CoA]", "MALONYL COA", allowAbstract = True)
malald      = smiles("OC(=O)CC=O", "MALONATE SEMIALDEHYDE")
HP3         = smiles("C(CO)C(=O)O", "3HP")
HP3CoA      = smiles("C(CO)C(=O)S[CoA]", "3-HYDROXYPROPIONATE COA", allowAbstract = True)
acryCoA     = smiles("C=CC(=O)S[CoA]", "ACRYLOYL COA", allowAbstract = True)
propCoA     = smiles("CCC(=O)S[CoA]", "PROPIONYL COA", allowAbstract = True)
metmalCoA   = smiles("CC(C(=O)O)C(=O)S[CoA]", "METHYLMALONYL COA", allowAbstract = True)

HPHB_eductmols = [
        succCoA,
        succald,
        HB4,
        HB4CoA,
        crotCoA,
        HB3CoA,
        acacetCoA,
        acCoA,
        malCoA,
        malald,
        HP3,
        HP3CoA,
        acryCoA,
        propCoA,
        metmalCoA
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
Fdred     = graphDFS("[Fdred]", "Fdred")
Fdox      = graphDFS("[Fdox]", "Fdox")


HPHB_helpermols = [
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
        Fdred,
        Fdox
        ]

### rules ###############################
# reaction 1 and 9
red_reduc_ = ruleGML("../rules/3HP4HB_reduction_reductase_succCoA_01.gml")

# reaction 2 and 10
red_dehydr_ = ruleGML("../rules/3HP4HB_reduction_dehydrogenase_01.gml")

# reaction 3 and 11
activ_synth_ = ruleGML("../rules/3HP4HB_activation_synthetase_01.gml")

# reaction 4
dehydr_4HB = ruleGML("../rules/3HP4HB_dehydration_4HBCoA_01.gml")

# reaction 5 
rehydr_crot = ruleGML("../rules/rTCA_dehydration_02_1.gml")

# reaction 6
oxi_dehydr_ = ruleGML("../rules/3HP4HB_oxidation_dehydrogenase_3HBCoA_01.gml")

# reaction 7
activ_trans_ = ruleGML("../rules/3HP4HB_transferase_acCoA_01_1.gml")

# reaction 8 and 14
carb_ = ruleGML("../rules/3HP4HB_carboxylation_ACC_01.gml")

# reaction 12
dehydr_3HP = ruleGML("../rules/3HP4HB_dehydration_3HPCoA_01.gml")

# reaction 13
red_reduc_acc = ruleGML("../rules/3HP4HB_reduction_reductase_acrylyl_01.gml")

# reaction 15
rearr_mutase = ruleGML("../rules/3HP4HB_rearrangement_mutase_01.gml")

## define ruleset
rset_3HP4HB = [
    red_reduc_,     # r1 & r9     
    red_dehydr_,    # r2 & r10   
    activ_synth_,   # r3 & r11   
    dehydr_4HB,     # r4
    rehydr_crot,    # r5   
    oxi_dehydr_,    # r6    
    activ_trans_,   # r7    
    carb_,          # r8 & r14
    dehydr_3HP,     # r12
    red_reduc_acc,  # r13    
    rearr_mutase    # r15
]