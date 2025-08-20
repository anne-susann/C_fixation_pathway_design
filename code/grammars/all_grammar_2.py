# ASABEL
# define space for all autocatalytic carbon fix pathways (molecules, cofactors)
# includes: rTCA, DC/4HB, 3HP/4HB, 3HPbicy, CBB, CETCH

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
## 3HP4HB
malCoA      = smiles("C(C(=O)O)C(=O)S[CoA]", "MALONYL COA", allowAbstract = True)
malald      = smiles("OC(=O)CC=O", "MALONATE SEMIALDEHYDE")
HP3         = smiles("C(CO)C(=O)O", "3HP")
HP3CoA      = smiles("C(CO)C(=O)S[CoA]", "3-HYDROXYPROPIONATE COA", allowAbstract = True)
acryCoA     = smiles("C=CC(=O)S[CoA]", "ACRYLYL COA", allowAbstract = True)
metmalCoA   = smiles("CC(C(=O)O)C(=O)S[CoA]", "METHYLMALONYL COA", allowAbstract = True)
## rTCA
ketogl      = smiles("C(CC(=O)O)C(=O)C(=O)O", "2-KETOGLUTARIC ACID")
isocit      = smiles("C(C(C(C(=O)O)O)C(=O)O)C(=O)O", "ISOCITRIC ACID")
aconi       = smiles("C(C(=CC(=O)O)C(=O)O)C(=O)O", "ACONITIC ACID")
citrate     = smiles("C(C(=O)O)C(CC(=O)O)(C(=O)O)O", "CITRIC ACID")
citCoA      = smiles("C(C(=O)O)C(CC(=O)S[CoA])(C(=O)O)O", "CITRYL COA", allowAbstract = True)
## 3HP bicycle
malylCoA    = smiles("C(C(C(=O)O)O)C(=O)S[CoA]", "MALYL COA", allowAbstract = True)
glyxo       = smiles("C(=O)C(=O)O", "GLYOXYLATE")
propCoA     = smiles("CCC(=O)S[CoA]", "PROPIONYL COA", allowAbstract = True)
metmalylCoA = smiles("CC(C(C(=O)O)O)C(=O)S[CoA]", "METHYLMALYL COA", allowAbstract = True)
mesaC1CoA   = smiles("CC(=CC(=O)O)C(=O)S[CoA]", "MESACONYL C1 COA", allowAbstract = True)
mesaC4CoA   = smiles("CC(=CC(=O)S[CoA])C(=O)O", "MESACONYL C4 COA", allowAbstract = True)
citmalCoA   = smiles("CC(CC(=O)S[CoA])(C(=O)O)O", "CITRAMALYL COA", allowAbstract = True)
## CETCH
ethmalCoA   = smiles("CCC(C(=O)O)C(=O)S[CoA]", "ETHYLMALONYL COA", allowAbstract = True)
metsuccCoA  = smiles("OC(=O)CC(C)C(=O)S[CoA]", "METHYLSUCCINYL COA", allowAbstract = True)

## CBB
ru1_5bp     = smiles("C(C(C(C(=O)COP(=O)(O)O)O)O)OP(=O)(O)O", "RIBULOSE-1,5-BISPHOSPHATE")
pga3        = smiles("C(C(C(=O)O)O)OP(=O)(O)O", "3-PHOSPHOGLYCERATE")
bpga1_3     = smiles("C(C(C(=O)OP(=O)(O)O)O)OP(=O)(O)O", "1,3-BISPHOSPHOGLYCERATE")
gap         = smiles("C(C(C=O)O)OP(=O)(O)O", "GAP")
dhap        = smiles("C(C(=O)COP(=O)(O)O)O", "DHAP")
f1_6bp      = smiles("C(C(C(C(C(=O)COP(=O)(O)O)O)O)O)OP(=O)(O)O", "FRUCTOSE-1,6-BISPHOSPHATE")
f1_6bp_r    = smiles("C(C1C(C(C(O1)(COP(=O)(O)O)O)O)O)OP(=O)(O)O", "FRUCTOSE-1,6-BISP_ring")
f6p         = smiles("C(C(C(C(C(=O)CO)O)O)O)OP(=O)(O)O", "FRUCTOSE-6-P")
e4p         = smiles("C(C(C(C=O)O)O)OP(=O)(O)O", "ERYTHROSE-4-P")
ru5p        = smiles("C(C(C(C(=O)CO)O)O)OP(=O)(O)O", "RIBULOSE-5-P")
x5p         = smiles("C(C(C(C(=O)CO)[xyO][H])O)OP(=O)(O)O", "XYLULOSE-5-P", allowAbstract = True)
s1_7bp      = smiles("C(C(C(C(C(C(=O)COP(=O)(O)O)O)O)O)O)OP(=O)(O)O", "SEDOHEPTULOSE-1,7-BISPHOSPHATE")
s7p         = smiles("C(C(C(C(C(C(=O)CO)O)O)O)O)OP(=O)(O)O", "SEDOHEPTULOSE-7-PHOSPHATE")
r5p         = smiles("C(C(C(C(C=O)O)O)O)OP(=O)(O)O", "RIBOSE-5-PHOSPHATE")

## alaline option of C4 glyoxylate
balanine    = smiles("C(CN)C(=O)O", "beta-ALANINE")
Lalanine    = smiles("CC(C(=O)O)N", "L-ALANINE")


# define eductmols
eductmols = [
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
        succ,
        malCoA,
        malald,
        HP3,
        HP3CoA,
        acryCoA,
        metmalCoA,
        ketogl,
        isocit,
        aconi,
        citrate,
        citCoA,
        malylCoA,
        glyxo,
        propCoA,
        metmalylCoA,
        mesaC1CoA,
        mesaC4CoA,
        citmalCoA,
        ethmalCoA,
        metsuccCoA,
        balanine,
        Lalanine,
        ru1_5bp,
        pga3,
        bpga1_3,
        gap,
        dhap,
        f1_6bp,
        # f1_6bp_r,
        f6p,
        e4p,
        ru5p,
        x5p,
        s1_7bp,
        s7p,
        r5p       
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
UQred     = graphDFS("O=[UQ]=O", "UQred")
UQox      = graphDFS("O[UQ]O", "UQox")
Fdred     = graphDFS("[Fdred]", "Fdred")
Fdox      = graphDFS("[Fdox]", "Fdox")
o2        = smiles("O=O", "O2")
h2o2      = smiles("OO", "H2O2")


# define helpermols
helpermols = [
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
        UQred,
        UQox,
        Fdred,
        Fdox,
        o2,
        h2o2
]

allKnown_mols = eductmols + helpermols

### rules ###############################

# all rules from the carbon fixation rules folder

# create ruleset 
## all rules from newly implemented pathways and less context rules

"""
import csv

def eductmols_dict(mols):
    list_of_dicts = []
    for mol in mols:
        dict = {"name": mol.name, "linearEncoding" :mol.linearEncoding, "id": mol.id}
        list_of_dicts.append(dict)
    return list_of_dicts

mol_dict = eductmols_dict(eductmols)

def create_look_up_eductmols(mols_dict, name, field_names):
    with open(f'data/{name}.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames = field_names)
        writer.writeheader()
        writer.writerows(mols_dict)

field_names = ["name", "linearEncoding", "id"]
create_look_up_eductmols(mol_dict, "eductmols_grammar_2", field_names)
"""

# rTCA
rule_01 = ruleGML('../rules/rTCA_activation_synthetase_01.gml') 
rule_02 = ruleGML('../rules/rTCA_activation_lysis_01.gml') 
rule_03 = ruleGML('../rules/rTCA_reduction_dehydrogenase_01.gml') 
rule_04 = ruleGML('../rules/rTCA_reduction_reductase_01.gml') 
rule_05 = ruleGML('../rules/rTCA_reduction_reductase_01_1.gml')
rule_06 = ruleGML('../rules/rTCA_reduction_reductase_01_2.gml') 
rule_07 = ruleGML('../rules/rTCA_dehydration_01.gml') 
rule_08 = ruleGML('../rules/rTCA_dehydration_02.gml') 
rule_09 = ruleGML('../rules/rTCA_dehydration_02_1.gml') 
rule_10 = ruleGML('../rules/rTCA_carboxylation_2KFOR_01.gml') 
rule_11 = ruleGML('../rules/rTCA_carboxylation_IDH_01.gml') 
rule_12 = ruleGML('../rules/rTCA_carboxylation_PEPC_01.gml')
rule_13 = ruleGML('../rules/rTCA_carboxylation_PEPC_01_1.gml')
rule_14 = ruleGML('../rules/rTCA_activation_dikinase_01.gml')  
rule_15 = ruleGML('../rules/rTCA_activation_dikinase_01_1.gml')   

# 3HP4HB
rule_16 = ruleGML('../rules/3HP4HB_dehydration_4HBCoA_01.gml')
rule_17 = ruleGML('../rules/3HP4HB_carboxylation_ACC_01.gml') 
rule_18 = ruleGML('../rules/3HP4HB_rearrangement_mutase_01.gml')  
rule_20 = ruleGML('../rules/3HP4HB_reduction_reductase_acrylyl_01.gml') 
rule_21 = ruleGML('../rules/3HP4HB_oxidation_dehydrogenase_3HBCoA_01.gml') 
rule_22 = ruleGML('../rules/3HP4HB_dehydration_3HPCoA_01.gml') 
rule_23 = ruleGML('../rules/3HP4HB_reduction_reductase_succCoA_01.gml') 
rule_24 = ruleGML('../rules/3HP4HB_reduction_dehydrogenase_01.gml') 
rule_25 = ruleGML('../rules/3HP4HB_activation_synthetase_01.gml') 
rule_19 = ruleGML('../rules/3HP4HB_transferase_acCoA_01.gml')
rule_26 = ruleGML('../rules/3HP4HB_transferase_acCoA_01_1.gml') 

# 3HPbicy
rule_27 = ruleGML('../rules/3HPbicy_transferase_mesaCoA_01.gml')
rule_28 = ruleGML('../rules/3HPbicy_activation_lysis_02.gml') 
rule_29 = ruleGML('../rules/3HPbicy_transferase_succCoA_malCoA_01.gml') 
rule_30 = ruleGML('../rules/3HPbicy_oxidation_dehydrogenase_succ_01.gml') 
rule_33 = ruleGML('../rules/3HPbicy_oxidation_dehydrogenase_succ_01_1.gml') 
rule_34 = ruleGML('../rules/3HPbicy_oxidation_dehydrogenase_succ_01_2.gml') 
rule_31 = ruleGML('../rules/3HPbicy_transferase_succCoA_a_01.gml') 
rule_36 = ruleGML('../rules/3HPbicy_transferase_succCoA_a_01_1.gml') 
rule_32 = ruleGML('../rules/3HPbicy_transferase_malCoA_b_01.gml') 
rule_35 = ruleGML('../rules/3HPbicy_transferase_malCoA_b_01_1.gml') 

# CBB
rule_37 = ruleGML('../rules/CBB_activation_bis_phosphatase_01.gml') 
rule_38 = ruleGML('../rules/CBB_activation_kinase_pga_01.gml') 
rule_39 = ruleGML('../rules/CBB_activation_kinase_ru5p_01.gml') 
rule_40 = ruleGML('../rules/CBB_carboxylation_rubisco_01.gml') 
rule_41 = ruleGML('../rules/CBB_epimerase_ru5p_01.gml') 
rule_42 = ruleGML('../rules/CBB_isomerase_01.gml') 
rule_43 = ruleGML('../rules/CBB_isomerase_02.gml') 
rule_44 = ruleGML('../rules/CBB_transketolase_01.gml')
rule_45 = ruleGML('../rules/CBB_reduction_dehydrogenase_gap_01.gml') 
rule_46 = ruleGML('../rules/CBB_aldolase_FBA_01.gml')

# CETCH
rule_47 = ruleGML('../rules/CETCH_activation_lysis_01_1.gml') 
rule_48 = ruleGML('../rules/CETCH_activation_lysis_02.gml') 
rule_49 = ruleGML('../rules/CETCH_carboxylation_ccr_01.gml') 
rule_50 = ruleGML('../rules/CETCH_dehydration_02_2.gml') 
rule_51 = ruleGML('../rules/CETCH_oxidation_oxidase_pco_01.gml') 
rule_52 = ruleGML('../rules/CETCH_rearrangement_mutase_01_1.gml') 

# GLYOXYLATE cycle
rule_53 = ruleGML('../rules/GLYOX_lysis_isocit_01.gml')
rule_54 = ruleGML('../rules/GLYOX_activation_synthase_mal_a_01.gml')
rule_55 = ruleGML('../rules/GLYOX_lysis_isocit_02.gml')
rule_56 = ruleGML('../rules/GLYOX_mutase_ala_01.gml') 
rule_57 = ruleGML('../rules/GLYOX_transaminase_01.gml')
rule_58 = ruleGML('../rules/GLYOX_transaminase_02.gml')
rule_59 = ruleGML('../rules/GLYOX_transferase_carboxy_malCoA_01.gml')


# for more context 
rset = [
        rule_01,
        rule_02,
        rule_03,
        rule_06,
        rule_07,
        rule_08,
        rule_09,
        rule_10,
        rule_11,
        rule_13,
        rule_15,
        rule_16,
        rule_17,
        rule_18,
        rule_20,
        rule_21,
        rule_22,
        rule_23,
        rule_24,
        rule_25,
        rule_26,
        rule_27,
        rule_28,
        rule_29,
        rule_30,
        rule_33,
        rule_34,
        rule_36,
        rule_35,
        # rule_37,
        # rule_38,
        # rule_39,
        # rule_40,
        # rule_41,
        # rule_42,
        # rule_43,
        # rule_44,
        # rule_45,
        # rule_46,
        rule_47,
        rule_48,
        rule_49,
        rule_50,
        rule_51,
        rule_52,
        rule_53,
        rule_54,
        rule_55,
        rule_56, 
        rule_57,
        rule_58,
        rule_59
]

# for less context
# replication of all_grammar_1
rset_less = [
        rule_01,
        rule_02,
        rule_03,
        rule_04,
        rule_07,
        rule_08,
        rule_09,
        rule_10,
        rule_11,
        rule_12,
        rule_14,
        rule_16,
        rule_17,
        rule_18,
        rule_19,
        rule_20,
        rule_21,
        rule_22,
        rule_23,
        rule_24,
        rule_25,
        rule_19,
        rule_27,
        rule_28,
        rule_29,
        rule_30,
        rule_31,
        rule_32
]

# all rules
rset_all = [
        rule_01,
        rule_02,
        rule_03,
        rule_04,
        rule_05,
        rule_06,
        rule_07,
        rule_08,
        rule_09,
        rule_10,
        rule_11,
        rule_12,
        rule_13,
        rule_14,
        rule_15,
        rule_16,
        rule_17,
        rule_18,
        rule_20,
        rule_21,
        rule_22,
        rule_23,
        rule_24,
        rule_25,
        rule_19,
        rule_26,
        rule_27,
        rule_28,
        rule_29,
        rule_30,
        rule_33,
        rule_34,
        rule_31,
        rule_36,
        rule_32,
        rule_35,
        rule_37,
        rule_38,
        rule_39,
        rule_40,
        rule_41,
        rule_42,
        rule_43,
        rule_44,
        rule_45,
        rule_46,
        rule_47,
        rule_48,
        rule_49,
        rule_50,
        rule_51,
        rule_52,
        rule_53,
        rule_54,
        rule_55,
        rule_59
]


print("####### len eductmols ##########")
print(len(eductmols))
print("####### len helpermols ##########")
print(len(helpermols))
print("####### len rset ##########")
print(len(rset))