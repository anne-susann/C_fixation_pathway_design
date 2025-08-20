# ASABEL
# analysis for energies, flows, and everything else

############## pre-processing #################
## import functions
import json
import pandas as pd
# import plotly as plt
import numpy as np

def open_json(file_name):
    with open(file_name, "r") as file:
        dictionary_or_list = json.load(file)
    return dictionary_or_list

def write_json(object_dict, output_file):
    with open(output_file, "w") as file:
        json.dump(object_dict, file, indent=4)

def open_txt_as_dict(file_name):
    solution_dict = {}
    with open(file_name, 'r') as file:
        for line in file:
            parts = line.split(',')
            key = parts[0].strip()
            value = int(parts[1].strip())
            solution_dict[key] = value
    return solution_dict


############## define input variable #################
# define which flow and which solutions to look at
# dg 2 steps expanded
dg_id = "gly_ala_2_2"

# flow query autocataylsis for acetyl CoA
flow_query = "3_difTarget_malate_1000"
# flow_query = "3_difTarget_1000"
# flow_query = "1_ac_enumerate_1000"

# cofactors included or not
cofactors = "_noATP"

# input directory of the flow query 
input_dir = "../energies"

# output directory for energy values
output_dir = "../energies"


###################################################
## topological analysis

# analyse how many cycles are in a flow solution

# --> cyclomatic number


# analyse origin of rules

# --> set of rules and set of molecules, then check set overlap with natural pathways

# analyse origin of molecules




###################################################
## energy analysis
energy_analysis = True

if energy_analysis == True:
    energies = open_json(f"{input_dir}/energy_flow_{flow_query}_dg_{dg_id}{cofactors}.json")
    all_energies = list(energies.values())
    # print(all_energies)

    mean_energies = np.mean(all_energies)
    print(mean_energies)
    std_energies = np.std(all_energies)
    print(std_energies)

    max_energies = np.max(all_energies)
    print(max_energies)
    min_energies = np.min(all_energies)
    print(min_energies)

    # save the values as text file
    with open(f"{output_dir}/summary_energy_flow_{flow_query}_dg_{dg_id}{cofactors}.txt", "w") as f:
        f.write(f"flow, {flow_query}\n")
        f.write(f"mean, {mean_energies}\n")
        f.write(f"standard deviation, {std_energies}\n")
        f.write(f"maximum, {max_energies}\n")
        f.write(f"minimum, {min_energies}\n") 

    # plot


## cofactor analysis
cofactor_analysis = False

if cofactor_analysis == True:
    cofactors_dict = open_txt_as_dict(f"{input_dir}/cofactors_flow_{flow_query}_dg_{dg_id}{cofactors}.txt")
    
    all_cofactors = list(cofactors_dict.values())
    # print(all_cofactors)

    mean_cofactors = np.mean(all_cofactors)
    print(mean_cofactors)
    std_cofactors = np.std(all_cofactors)
    print(std_cofactors)

    max_cofactors = np.max(all_cofactors)
    print(max_cofactors)
    min_cofactors = np.min(all_cofactors)
    print(min_cofactors)

    # save the values as text file
    with open(f"{output_dir}/summary_cofactors_flow_{flow_query}_dg_{dg_id}{cofactors}.txt", "w") as f:
        f.write(f"flow, {flow_query}\n")
        f.write(f"mean, {mean_cofactors}\n")
        f.write(f"standard deviation, {std_cofactors}\n")
        f.write(f"maximum, {max_cofactors}\n")
        f.write(f"minimum, {min_cofactors}\n") 
