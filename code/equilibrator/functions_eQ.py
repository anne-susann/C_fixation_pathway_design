# ASABEL
# utility functions

# import dependencies
import csv

###############################
## dictionaries

# print csv of dict of all eductmols
def create_look_up_molecules(mols_dict, name):
    with open(f'data/{name}.csv', 'w') as f:
        writer = csv.writer(f)
        for molName, linEnc in mols_dict.items():
             writer.writerow([molName, linEnc])

# save Look-up Dictionary as external file
def create_look_up_energies(mols_dict, name):
    with open(f'data/{name}.csv', 'w') as f:
        writer = csv.writer(f)
        for molName, data in mols_dict.items():
             writer.writerow([molName, data])

# open csv of all eductmols
def open_molecules(filename):
# for molecules as keys and smiles as values         
    molecules = {}
    with open(f"data/{filename}.csv", mode='r') as infile:
        reader = csv.reader(infile)
        for rows in reader:
            print(rows[0])
            key = rows[0]
            value = rows[1]
            molecules[key] = value
        print(molecules)

###############################
## create and/or search for compounds

### get or create ###

def getEQObjectOfMolecule(molName, dict_name):
# finds or 
# requires molecules in dictonary as moleclues{ name : smiles}
    smiles = molecules[molName]
    object_cpd = get_or_create_compounds(cc.ccache, [smiles], mol_format="smiles")[0].compound
    print(object_cpd)
    energy = get_standard_dgf_prime(object_cpd)
    if object_cpd.id < 0:
        print("Compound not found in equilibrator-cache")
        print(f"∆fG'° of generated compound: {get_standard_dgf_prime(object_cpd)}")
    else:
        print(f"Found compound in equilibrator-cache: ID = {object_cpd.id}, name = {object_cpd.get_common_name()}")
        print(f"∆fG'° of cached compound: {get_standard_dgf_prime(object_cpd)}")
    inchi_key = object_cpd.inchi_key
    dict_name[molName] = [smiles, inchi_key, energy]

### create ###

def createEQObjectOfMolecule(molName, dict_name):
# CREATES a compound by smiles string
# requires molecules in dictonary as moleclues{ name : smiles}
    smiles = molecules[molName]
    object_cpd = create_compounds([smiles], mol_format="smiles")[0].compound
    print(object_cpd)
    energy = get_standard_dgf_prime(object_cpd)
    if object_cpd.id < 0:
        print("Compound not found in equilibrator-cache")
        print(f"∆fG'° of generated compound: {get_standard_dgf_prime(object_cpd)}")
    else:
        print(f"Found compound in equilibrator-cache: ID = {object_cpd.id}, name = {object_cpd.get_common_name()}")
        print(f"∆fG'° of cached compound: {get_standard_dgf_prime(object_cpd)}")
    inchi_key = object_cpd.inchi_key
    dict_name[molName] = [smiles, inchi_key, energy]

### by Name ###

def getEQObjectOfMolecule_byName(molName, dict_name, input_name):
# finds OR creates a compound by NAME OF MOLECULE
# requires molecules in dictonary as moleclues{ name : smiles}   
    object_cpd = cc.search_compound(molName)
    print(object_cpd)
    energy = get_standard_dgf_prime(object_cpd)
    if object_cpd.id < 0:
        print("Compound not found in equilibrator-cache")
        print(f"∆fG'° of generated compound: {get_standard_dgf_prime(object_cpd)}")
    else:
        print(f"Found compound in equilibrator-cache: ID = {object_cpd.id}, name = {object_cpd.get_common_name()}")
        print(f"∆fG'° of cached compound: {get_standard_dgf_prime(object_cpd)}")
    inchi_key = object_cpd.inchi_key
    smiles = input_name[molName]
    dict_name[molName] = [smiles, inchi_key, energy]


###############################
## generel utils

# save lists of dg objects as csv object
def create_look_up(list_of_objects, name):
    # vertices = []
    # for v in dg.vertices:
    #     vertices.append([v.graph.name])
    with open(f'data/{name}.csv', 'w') as f:
        write = csv.writer(f)
        write.writerows(list_of_objects)


# Energy getter function
def getEnergy(molName, dict_name):
    return dict_name.get(molName)[2]

