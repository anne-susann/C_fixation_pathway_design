# ASABEL
# post processing annotation of flow solutions with energy

############## pre-processing #################
## import functions
import json
import csv
# import pandas as pd
include("../utils/functions_co2_01.py")


############## define input variable #################
# define which flow and which solutions to look at
# dg 2 steps expanded
dg_id = "gly_ala_2_2"

# flow query autocataylsis for acetyl CoA
flow_query = "3_difTarget_malate_1000"

# input directory of the flow query 
input_dir = "../1000_sol"

# output directory for energy values
output_dir = "../energies"

################ define which operations to run ###############

# formatting the energy dictionary (only needed once)
start_energy_dict_formatting = False

# caclulating overall dG for solutions
start_calculate_dG_overall = False

# caclulating dG WITHOUT COFACTORS 
start_calculate_dG_noCofactors = True

# count cofactors 
counting_cofactors = False

# annotate solution for every edge

# turn into presentable table


################ define functions ###############

def open_json(file_name):
    with open(file_name, "r") as file:
        dictionary_or_list = json.load(file)
    return dictionary_or_list

def write_json(object_dict, output_file):
    with open(output_file, "w") as file:
        json.dump(object_dict, file, indent=4)



###############################################################
## turn current output into energy dictionary of the form name: [energy, deviation, unit]


if start_energy_dict_formatting == True:

    ########## import energies of formation to molecules ##########
    # import energy look up table 
    energies = open_json("../look_up/look-up_all_energy_dict.json")

    # load linenc to name dictionary
    dictionary_names_to_linenc = {}
    with open("../look_up/linenc_all_unknown_noCBB_gly_ala_2_5.csv", mode='r') as infile:
        reader = csv.reader(infile)
        for rows in reader:
            key = rows[0] 
            linEnc = rows[1]  
            dictionary_names_to_linenc[key] = linEnc


    ###### transform the energies dictionary to contain names and numbers

    energies_helpermols = open_json("../look_up/look-up_helpermols_energy_dict.json")

    energies_known = open_json("../look_up/look-up_known_energy_dict.json")

    energies_known.update(energies_helpermols)


    ##### open the look-up that has the linear encoding, smiles, and names ######
    unknown_translation_dict = {}
    # its three entries per row, I need the first and the third, so row[0] and row[2]
    with open("../look_up/look-up_unknown_gly_ala_2_5_WICHTIG.csv", mode='r', newline='') as unknown_energies:
        reader = csv.reader(unknown_energies,quotechar="'", delimiter=",", quoting=csv.QUOTE_ALL, skipinitialspace=True)

        for row in reader: 
            key = row[0] # linear encoding from mod (including [CoA])
            value_name = row[2] # name of the molecule
            unknown_translation_dict[key] = value_name
            # print(unknown_energies_dict)
    linenc_unknown = unknown_translation_dict.keys()
    # print(linenc_unknown)


    ## convert the dictionaries
    convertEnergyDB()
            
###############################################################
## start annotation workflow


########## import energy dictionary name:[energy, deviation, unit] ##########
energy_dictionary = open_json("new_look_up_energies_all_names.json")
# print(energy_dictionary)


########## import overall reaction of solutions ##########
overall_reactions_solutions = open_json(f"{input_dir}/overall_reactions_{dg_id}_{flow_query}.json")


########## calculate overall dG for network ##########
# Simplest version: energy of the network is
# total output energies of formation - total input energies of formation


if start_calculate_dG_overall == True: 

    dG_overall = calculate_dG_overall(overall_reactions_solutions, energy_dictionary, output_dir)
    print(dG_overall)



########## calculate dG EXCLUDING ATP ##########


if start_calculate_dG_noCofactors == True:

    dG_overall_noATP = calculate_dG_overall_noATP(overall_reactions_solutions, energy_dictionary, output_dir)
    print(dG_overall_noATP)


# count cofactors in solutions
def count_cofactors(solutions_overall_inflow_outflow):

    cofactors_total = {}

    energy_cofactors = ["ATP", "ADP", "AMP", "PPi", "Pi"]
    redox_cofactors = ["Fdox", "Fdred", "NAD+", "NADH", "NADP+", "NADPH", "UQox", "UQred"]

    # iterate through solutions
    for solution_index, solution in enumerate(solutions_overall_inflow_outflow):
        print(f"============= count cofactors for solution_{solution_index} =============")
        print(solutions_overall_inflow_outflow[solution])
        
        # to iterate over next level of dictionary, define the solution_x as the working dict
        solution_x = solutions_overall_inflow_outflow[solution]

        # count cofactors
        cofactors_in = 0
        cofactors_out = 0

        # iterate through the flows, then devide between in and out flow
        for flow in solution_x:    
            print(flow)

            # to iterate over next level of dictionary, define flow_x as the working dict
            flow_x = solution_x[flow]

            # first work on the inflow
            if flow == "inflow":
                # go through inflows and find the energy 
                for mol in flow_x:

                    ## check if ATP, ADP, AMP, PPi, Pi
                    if mol in energy_cofactors:
                        print(mol)
                        multiplier = int(flow_x[mol])
                        
                        cofactors_in += 1 * multiplier
                    
                    if mol in redox_cofactors:
                        print(mol)
                        multiplier = int(flow_x[mol])
                        cofactors_in += 1 * multiplier

            # check the cofactors
            if flow == "inflow":
                print(cofactors_in)
        

            cofactors_total[f"solution_{solution_index}"] = cofactors_in

    with open(f"{output_dir}/cofactors_flow_{flow_query}_dg_{dg_id}.txt", "w") as f:
        for solution_index, solution in enumerate(solutions_overall_inflow_outflow):
            value = f"solution_{solution_index}"
            f.write(f"solution_{solution_index}, {cofactors_total[value]}\n")

    return cofactors_total

# overall_reactions_solutions = open_json(f"{input_dir}/overall_reactions_{dg_id}_{flow_query}.json")

if counting_cofactors == True:

    count_cofactors(overall_reactions_solutions)

###############################################################
## turn annotations into nice graphs and plots





'''
Table should contain

                Steps       ATP usage   other cofactors         energy              Novel Mols      Autocatalytic molecules      Objective function
flow 1  sol_0   No. edges   No. ATP     No. Redox_cofactors     with or without     as part of sol   acetyl-CoA/ Propionyl-CoA      shortest path
                                                                cofactors?
        sol_1
        sol_2
flow 2  sol_0
        sol_1
        sol_2
flow 3  sol_0
        sol_1
        sol_2

Natural pathways
CETCH
HOPAC
Bar Even
        

'''













###############################################################
########## calculate dG for each edge ##########
## with c = 1 mM
## for steady state literally just dG0, so energies of formation of the input/output

# reaction energy at standard conditions for each reaction
# dG0_r1 = (dGf_product_1 + dGf_product_2) - (dGf_reactant_1 + dGf_reactant_2)
# dG0_r1 = sum(dGf_products) - sum(dGf_reactants)

# overall energy of the network
# dGtotal = dG0_r1 + dG0_r2 + ... + dG0_rx

########## import dg, edge list, vertex list ##########
# import edges of all flow solutions
# with open(f"../data/edges_flowq_{flow_query}_solutions_{dg_id}.json", "r") as file:
#     flow_edges_data = json.load(file)

# print(flow_edges_data)

# import vertices of all flow solutions
# with open(f"../data/vertices_flowq_{flow_query}_solutions_{dg_id}.json", "r") as file:
#     flow_vertices_data = json.load(file)

# print(flow_vertices_data)

########## annotate molecules with dGf ##########
'''
# this would be for step wise calculation of the individual reactions
for sol, solution_id in solutions:
    annotated_edges = {}
  
    for edge in sol:
        annotated_in = {}
        annotated_out = {}
  
        for mol in sol[inflow]:
            if mol in energies.keys:
                energy = energies[mol]
                annotated_inflow.append = [mol, energy]
                
            elif mol in names_to_linenc:
                linenc = names_to_linenc[mol]
                energy = energies[linenc]
                annotated_inflow.append = [mol, energy]
  
        annotated_in[inflow] = annotated_inflow    
  
        for mol in sol[outflow]:
            if mol in energies.keys:
                energy = energies[mol]
                annotated_outflow = [mol, energy]
                
            elif mol in names_to_linenc:
                linenc = names_to_linenc[mol]
                energy = energies[linenc]
                annotated_outflow = [mol, energy]
        annotated_out[outflow] = annotated_outflow    

   flow_info = flow_edges_info[flow_on_edge]
'''

"""

def calculate_dG0_reaction(json):

    for solution in json:
        for edge in solution:
            dGf_products = 0
            dGf_reactants = 0

            for mol in inflow:
                dGf_reactants =+ convertedEnergyDB[mol](0)
            for mol in outflow:
                dGf_products =+ convertedEnergyDB[mol](0)

            reaction_energy = dGf_products - dGf_reactants

            edge["reaction_energy"] = reaction_energy


def calculate_dG_solution(json):

    for solution in json:
        dG_total = 0
        for edge in solution:
            dG_total =+ edge[reaction_energy]

        print(dG_total)
        solution["dG_total"] = dG_total
        
    
"""


