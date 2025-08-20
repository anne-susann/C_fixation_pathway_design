# ASABEL
# define space for the 3HP bicycle (molecules, cofactors)

### molecules ###############################

## starter molecules
## 3HP bicycle
succCoA     = smiles("OC(=O)CCC(=O)S[CoA]", "SUCCINYL COA", allowAbstract = True)
succ        = smiles("OC(=O)CCC(=O)O", "SUCCINIC ACID")
fumarate    = smiles("C(=CC(=O)O)C(=O)O", "FUMARIC ACID")
malate      = smiles("C(C(C(=O)O)O)C(=O)O", "MALIC ACID")
malylCoA    = smiles("C(C(C(=O)O)O)C(=O)S[CoA]", "MALYL COA", allowAbstract = True)
glyxo       = smiles("C(=O)C(=O)O", "GLYOXYLATE")
propCoA     = smiles("CCC(=O)S[CoA]", "PROPIONYL COA", allowAbstract = True)
metmalylCoA = smiles("CC(C(C(=O)O)O)C(=O)S[CoA]", "METHYLMALYL COA", allowAbstract = True)
mesaC1CoA   = smiles("CC(=CC(=O)O)C(=O)S[CoA]", "MESACONYL C1 COA", allowAbstract = True)
mesaC4CoA   = smiles("CC(=CC(=O)S[CoA])C(=O)O", "MESACONYL C4 COA", allowAbstract = True)
citmalCoA   = smiles("CC(CC(=O)S[CoA])(C(=O)O)O", "CITRAMALYL COA", allowAbstract = True)
pyruv       = smiles("CC(=O)C(=O)O", "PYRUVATE")
acCoA       = smiles("CC(=O)S[CoA]", "ACETYL COA", allowAbstract = True)
malCoA      = smiles("C(C(=O)O)C(=O)S[CoA]", "MALONYL COA", allowAbstract = True)
malald      = smiles("OC(=O)CC=O", "MALONATE SEMIALDEHYDE")
HP3         = smiles("C(CO)C(=O)O", "3HP")
HP3CoA      = smiles("C(CO)C(=O)S[CoA]", "3-HYDROXYPROPIONATE COA", allowAbstract = True)
acryCoA     = smiles("C=CC(=O)S[CoA]", "ACRYLOYL COA", allowAbstract = True)
metmalCoA   = smiles("CC(C(=O)O)C(=O)S[CoA]", "METHYLMALONYL COA", allowAbstract = True)

HP3bicy_eductmols = [
        succCoA,
        succ,
        fumarate,
        malate,
        malylCoA,
        glyxo,
        propCoA,
        metmalylCoA,
        mesaC1CoA,
        mesaC4CoA,
        citmalCoA,
        pyruv,
        acCoA,
        malCoA,
        malald,
        HP3,
        HP3CoA,
        acryCoA,
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
UQred     = graphDFS("O=[UQ]=O", "UQred")
UQox      = graphDFS("O[UQ]O", "UQox")
hco3      = smiles("C(=O)(O)[O-]", "HCO3-")
co2       = smiles("C(=O)=O", "CO2")

HP3bicy_helpermols = [
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
        UQred,
        UQox,
        hco3,
        co2
        ]

### rules ###############################
# reaction 1 and 4
activ_trans_CoA = ruleGML("../rules/3HPbicy_transferase_succCoA_malCoA_01.gml")
# reaction 1 (two rules)
activ_trans_succCoA = ruleGML("../rules/3HPbicy_transferase_succCoA_a_01_1.gml")

# reaction 2
oxi_dehydr_succ = ruleGML("../rules/3HPbicy_oxidation_dehydrogenase_succ_01_2.gml")

# reaction 3 
rehydr_malate = ruleGML("../rules/rTCA_dehydration_02_1.gml")

# reaction 4 (two rules)
activ_trans_malCoA = ruleGML("../rules/3HPbicy_transferase_malCoA_b_01_1.gml")

# reaction 5 and 10
activ_lysis_ = ruleGML("../rules/rTCA_activation_lysis_01.gml")

# reaction 6
activ_lysis_rev = ruleGML("../rules/3HPbicy_activation_lysis_02.gml")

# reaction 7 and 15
dehydr_ = ruleGML("../rules/3HP4HB_dehydration_3HPCoA_01.gml")

# reaction 8
rearr_trans_mesa = ruleGML("../rules/3HPbicy_transferase_mesaCoA_01.gml")

# reaction 9
rehydr_mesa = ruleGML("../rules/rTCA_dehydration_02_1.gml")

## 3HP4HB part of pathway
# reaction 11 and 17
carb_ = ruleGML("../rules/3HP4HB_carboxylation_ACC_01.gml")

# reaction 12
red_reduc_ = ruleGML("../rules/3HP4HB_reduction_reductase_succCoA_01.gml")

# reaction 13
red_dehydr_ = ruleGML("../rules/3HP4HB_reduction_dehydrogenase_01.gml")

# reaction 14
activ_synth_ = ruleGML("../rules/3HP4HB_activation_synthetase_01.gml")

# reaction 16
red_reduc_acc = ruleGML("../rules/3HP4HB_reduction_reductase_acrylyl_01.gml")

# reaction 18
rearr_mutase = ruleGML("../rules/3HP4HB_rearrangement_mutase_01.gml")

## define ruleset
rset_3HPbicy = [
        activ_trans_CoA,        # r1 & r4
        activ_trans_succCoA,    # r1 (two rules)
        oxi_dehydr_succ,        # r2
        rehydr_malate,          # r3
        activ_trans_malCoA,     # r4 (two rules)
        activ_lysis_,           # r5 & 10
        activ_lysis_rev,        # r6 
        dehydr_,                # r7 & 15
        rearr_trans_mesa,       # r8
        rehydr_mesa,            # r9
        carb_,                  # r11 & 17
        red_reduc_,             # r12
        red_dehydr_,            # r13
        activ_synth_,           # r14
        red_reduc_acc,          # r16
        rearr_mutase            # r18
]