# ASABEL
# plot the outcomes of the analysis workflows

### import packages ###
import json
# import pandas as pd
# import plotly as plt
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 22})

### define functions ###
def open_json(file_name):
    with open(file_name, "r") as file:
        dictionary_or_list = json.load(file)
    return dictionary_or_list

def open_txt_as_dict(file_name):
    solution_dict = {}
    with open(file_name, 'r') as file:
        for line in file:
            parts = line.split(',')
            key = parts[0].strip()
            value = int(parts[1].strip())
            solution_dict[key] = value
    return solution_dict


################# energies ###############
### import data ###
energies_1_ac_enumerate = open_json(f"../energies/energy_flow_1_ac_enumerate_1000_dg_gly_ala_2_2.json")
energies_3_difTarget = open_json(f"../energies/energy_flow_3_difTarget_1000_dg_gly_ala_2_2.json")
energies_3_difTarget_malate = open_json(f"../energies/energy_flow_3_difTarget_malate_1000_dg_gly_ala_2_2.json")

# Prepare figure
# plt.figure(figsize=(8, 5))

# Plot each dataset with a unique color and label
# for i, (label, data) in enumerate({
#     "AC acetyl-CoA": energies_1_ac_enumerate,
#     "AC propionyl-CoA": energies_3_difTarget,
#     "AC malate": energies_3_difTarget_malate
# }.items()):
#     x = [int(k.split('_')[1]) for k in data.keys()]
#     y = list(data.values())
#     plt.scatter(x, y, label=label)

# # Add labels, legend, grid
# plt.xlabel("Solution Number")
# plt.ylabel("Energy Value")
# plt.title("Comparison of Energy Values by Solution")
# plt.legend()
# plt.grid(True)
# plt.tight_layout()
# plt.savefig("energies_1000_plot.png", dpi=300)
# plt.show()



############### cofactors ############
cofactors_1_ac_enumerate = open_txt_as_dict(f"../energies/cofactors_flow_1_ac_enumerate_1000_dg_gly_ala_2_2.txt")
cofactors_3_difTarget = open_txt_as_dict(f"../energies/cofactors_flow_3_difTarget_1000_dg_gly_ala_2_2.txt")
cofactors_3_difTarget_malate = open_txt_as_dict(f"../energies/cofactors_flow_3_difTarget_malate_1000_dg_gly_ala_2_2.txt")

# # plot
# plt.figure(figsize=(8, 5))

# # Plot each dataset with a unique color and label
# for i, (label, data) in enumerate({
#     "AC acetyl-CoA": cofactors_1_ac_enumerate,
#     "AC propionyl-CoA": cofactors_3_difTarget,
#     "AC malate": cofactors_3_difTarget_malate
# }.items()):
#     x = [int(k.split('_')[1]) for k in data.keys()]
#     y = list(data.values())
#     plt.scatter(x, y, label=label)

# # Add labels, legend, grid
# plt.xlabel("Solution Number")
# plt.ylabel("Cofactor Amount")
# plt.title("Comparison of Energy Values by Solution")
# plt.legend()
# plt.grid(True)
# plt.tight_layout()
# plt.savefig("cofactors_1000_plot.png", dpi=300)
# plt.show()

### plot the overview ###

def calculate_mean_std(data):
    mean = np.mean(data)
    std = np.std(data)
    max = np.max(data)   
    min = np.min(data)
    return [mean, std, max, min]
  
## energies
overview_en_1_ac_enumerate_1000 = calculate_mean_std(list(energies_1_ac_enumerate.values()))
overview_en_3_difTarget = calculate_mean_std(list(energies_3_difTarget.values()))
overview_en_3_difTarget_malate = calculate_mean_std(list(energies_3_difTarget_malate.values()))

## cofactors
overview_co_1_ac_enumerate_1000 = calculate_mean_std(list(cofactors_1_ac_enumerate.values()))
overview_co_3_difTarget = calculate_mean_std(list(cofactors_3_difTarget.values()))
overview_co_3_difTarget_malate = calculate_mean_std(list(cofactors_3_difTarget_malate.values()))


#### overview all together ####
# plt.figure(figsize=(8, 5))
# plt.errorbar("AC acetyl-CoA", overview_en_1_ac_enumerate_1000[0], yerr=overview_en_1_ac_enumerate_1000[1], fmt='o', label='AC acetyl-CoA energy', capsize=5)
# plt.errorbar("AC acetyl-CoA", overview_co_1_ac_enumerate_1000[0], yerr=overview_co_1_ac_enumerate_1000[1], fmt='o', label='AC acetyl-CoA cofactor', capsize=5)

# plt.errorbar("AC propionyl-CoA", overview_en_3_difTarget[0], yerr=overview_en_3_difTarget[1], fmt='o', label='AC propionyl-CoA energy', capsize=5)
# plt.errorbar("AC propionyl-CoA", overview_co_3_difTarget[0], yerr=overview_co_3_difTarget[1], fmt='o', label='AC propionyl-CoA cofactor', capsize=5)

# plt.errorbar("AC malate", overview_en_3_difTarget_malate[0], yerr=overview_en_3_difTarget_malate[1], fmt='o', label='AC malate energy', capsize=5)
# plt.errorbar("AC malate", overview_co_3_difTarget_malate[0], yerr=overview_co_3_difTarget_malate[1], fmt='o', label='AC malate cofactor', capsize=5)

# # Customize
# plt.xlabel("Query Type")
# plt.ylabel("Value")
# plt.title("Mean ± Standard Deviation of Energies and Cofactors")
# plt.legend()
# plt.grid(True)
# plt.savefig("overview_1000_runs_energy_cofactors_plot.png", dpi=300, bbox_inches='tight')
# plt.show()

#### overview ONLY energies ####
plt.figure(figsize=(12, 8))
plt.errorbar(
    "AC Acetyl-CoA", 
    overview_en_1_ac_enumerate_1000[0], 
    yerr=overview_en_1_ac_enumerate_1000[1], 
    fmt='o', 
    label='AC acetyl-CoA energy', 
    capsize=5,

    color = "#CC79A7",
    ecolor = "#CC79A7",
    elinewidth= 4,
    linewidth = 4,
    capthick = 3,
    markersize = 11
    )

plt.errorbar(
    "AC Propionyl-CoA", 
    overview_en_3_difTarget[0], 
    yerr=overview_en_3_difTarget[1], 
    fmt='o', 
    label='AC propionyl-CoA energy', 
    capsize=5,

    color = "#0072B2",
    ecolor = "#0072B2",
    elinewidth= 4,
    linewidth = 4,
    capthick = 3,
    markersize = 11
    )

plt.errorbar(
    "AC Malate", 
    overview_en_3_difTarget_malate[0], 
    yerr=overview_en_3_difTarget_malate[1], 
    fmt='o', 
    label='AC malate energy', 
    capsize=5,
    
    color = "#D55E00",
    ecolor = "#D55E00",
    elinewidth= 4,
    linewidth = 4,
    capthick = 3,
    markersize = 11
    )

# Customize
# plt.xlabel("Query Type")
plt.ylabel("Energy $\Delta$ G [kJ/mol]")
plt.title("Energy values compared between flow queries", pad = 12) #changed pad
# plt.legend()
plt.grid(True)
plt.savefig("overview_1000_runs_energy_plot.png", dpi=300, bbox_inches='tight')
plt.show()

#### overview ONLY cofactors ####
plt.figure(figsize=(12, 8))
plt.errorbar(
    "AC Acetyl-CoA", 
    overview_co_1_ac_enumerate_1000[0], 
    yerr=overview_co_1_ac_enumerate_1000[1], 
    fmt='o', 
    label='AC acetyl-CoA cofactor', 
    capsize=5,
    
    color = "#CC79A7",
    ecolor = "#CC79A7",
    elinewidth= 4,
    linewidth = 4,
    capthick = 3,
    markersize = 11
    )

plt.errorbar(
    "AC Propionyl-CoA",
    overview_co_3_difTarget[0], 
    yerr=overview_co_3_difTarget[1], 
    fmt='o', 
    label='AC propionyl-CoA cofactor', 
    capsize=5,
    
    color = "#0072B2",
    ecolor = "#0072B2",
    elinewidth= 4,
    linewidth = 4,
    capthick = 3,
    markersize = 11
    )

plt.errorbar(
    "AC Malate", 
    overview_co_3_difTarget_malate[0], 
    yerr=overview_co_3_difTarget_malate[1], 
    fmt='o', 
    label='AC malate cofactor', 
    capsize=5,
    
    color = "#D55E00",
    ecolor = "#D55E00",
    elinewidth= 4,
    linewidth = 4,
    capthick = 3,
    markersize = 11
    )

# Customize
# plt.xlabel("Query Type")
plt.ylabel("Number of cofactors")
plt.title("Number of cofactors compared between flow queries", pad = 12)
# plt.legend()
plt.grid(True)
plt.savefig("overview_1000_runs_cofactors_plot.png", dpi=300, bbox_inches='tight')
plt.show()
