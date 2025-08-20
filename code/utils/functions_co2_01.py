# ASABEL
# utility functions

# import dependencies
import csv
import re
import json

##############################################################
## generel utils

# print all rules in rule directory
def print_all_rules(ruledir):
    files = os.listdir(ruledir)
    rules = [file for file in files if file.endswith(".gml")]
    a = [ruleGML(ruledir + gml) for gml in rules]
    post.summarySection("DPO Diagrams of Rule(s)")
    for r in a:
        p = GraphPrinter()
        p.setReactionDefault()
        p.withIndex = True
        r.print(p)

# create dict of molecules with names and smiles/graphDFS
# def molecules_dict(mols):
# # creates a list of dictionaries
#     list_of_dicts = []
#     for mol in mols:
#         dict = {"name": mol.name, "linearEncoding" :mol.linearEncoding, "id": mol.id}
#         list_of_dicts.append(dict)
#     return list_of_dicts

def molecules_dict(mols):
# creates one dictionary with the key being name of molecule
    dict = {}
    for mol in mols:
        dict.update({mol.name: mol.linearEncoding})
    return dict

# print csv of all molecules
# def create_look_up_molecules(mols_dict, name, field_names):
# # for creating a look up table from a list of dictionaries
#     with open(f'data/{name}.csv', 'w') as f:
#         writer = csv.DictWriter(f, fieldnames = field_names)
#         writer.writeheader()
#         writer.writerows(mols_dict)

## create a lookup table for the molecule dictionary
def create_look_up_molecules(mols_dict, name):
    with open(f'data/{name}.csv', 'w') as f:
        writer = csv.writer(f)
        for molName, linEnc in mols_dict.items():
             writer.writerow([molName, linEnc])


# # open csv of all molecules
# def open_look_up_molecules(file):
# # for a list of dictionaries
#     with open(f"data/{file}.csv", 'r') as f:
#         list_of_dicts = list(csv.DictReader(f))
#     return list_of_dicts


def open_look_up_molecules(filename):
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
    return molecules
    

def read_eQ_csv_measurement_as_dict(input_file):
# for reading csv files created by eQuilibrator output with the Measurment entry
# SPECIFICALLY MADE FOR <Measurement(value, error, kilojoule/mol)>
    dictionary = {}

    # Open and read the CSV file
    with open(input_file, mode='r') as infile:
        reader = csv.reader(infile)
        
        for rows in reader:
            key = rows[0] # Use the first column as the dictionary key
            value_str = rows[1]  
            
            # Manually parse the SMILES and InChI key
            smiles_inchi = re.findall(r"'(.*?)'", value_str)  # Find strings in single quotes
            if len(smiles_inchi) < 2:
                print(f"Skipping rows due to unexpected format: {rows}")
                continue
            
            smiles = smiles_inchi[0]
            inchi_key = smiles_inchi[1]
            
            # Extract energy data from Measurement 
            energy_match = re.search(r"<Measurement\(([-\d.]+), ([-\d.]+), (\w+ / \w+)\)>", value_str)
            if energy_match:
                # Parse the Measurement values into a list
                energy = [
                    float(energy_match.group(1)),  # Value
                    float(energy_match.group(2)),  # Uncertainty
                    energy_match.group(3)          # Unit
                ]
            else:
                energy = None 
            
            # Combine the values into a list 
            dictionary[key] = [smiles, inchi_key, energy]

    return dictionary


def read_eQ_csv_as_dict(input_file):
# for reading csv files created by eQuilibrator output GENERGIC FORMAT
    dictionary = {}

    # Open and read the CSV file
    with open(input_file, mode='r') as infile:
        reader = csv.reader(infile)
        
        for rows in reader:
            # original graphDFS
            key = rows[0] 
            # output from eQuilibrator
            energy_value = rows[1]  
            energy_error = rows[2]
            smiles = rows[3]
            inchi_key = rows[4]
                   
            # Combine the values into a list, to make it look like the previous lists use the following order
            dictionary[key] = [ smiles, inchi_key, [energy_value, energy_error]]

    return dictionary


##############################################################
## utils for dg expansion

# by Nino
# using only specified rules and building dg step by step
def educt_product(univ, educt, product, rule):
    return (addUniverse(univ)
                >> addSubset(educt) 
                >> leftPredicate[lambda d: educt in d.left](
                    rightPredicate[lambda d: product in d.right](rule)
                )
            )

##############################################################
## utils for dg printer 

# by Nino
def is_in_graphlist(molgraph,graphlist):
    """ check if certain graph is in a graph-list """
    for g in graphlist:
        if molgraph.isomorphism(g) > 0:
            return True
    return False

# by Nino
def hide_mols(graphlist,pr=DGPrinter()):
    """
    retrun DGprinter() that hides all nodes defined in graphlist
    """
    pr.pushVertexVisible(lambda v: not is_in_graphlist(v.graph, graphlist))
    return pr

# print input rules
def print_input_rules(rlist = inputRules):
    for r in rlist:
        p = GraphPrinter()
        p.setReactionDefault()
        p.withIndex = True
        r.print(p)


##############################################################
## utils for dgs

# display the size of a dg by vertices and edges
def display_size_dg(dg):
    print("############ No vertices ############")
    print(dg.numVertices)
    print("============ No edges ============")
    print(dg.numEdges)


# print a list of nodes from a derivation graph
# iterate over dg object to list all nodes
def dg_edges(dg):
    edges = []
    print(f"============| edges |================")
    for e in dg.edges:
        print([c.graph.name for c in e.sources],[c.graph.name for c in e.targets])
        edges.append(([c.graph.name for c in e.sources],[c.graph.name for c in e.targets]))
    print("============================")
    return edges 

    
# iterate over dg object to list all vertices
def dg_vertices(dg):
    vertices = []
    print(f"############| vertices |################")
    for v in dg.vertices:
        print([v.graph.name])
        vertices.append([v.graph.name])
    print("############################")
    return vertices


# save lists of dg objects as csv object
def create_look_up(list_of_objects, name):
    # vertices = []
    # for v in dg.vertices:
    #     vertices.append([v.graph.name])
    with open(f'data/{name}.csv', 'w') as f:
        write = csv.writer(f)
        write.writerows(list_of_objects)


# load list of dg objects
"""
def load_look_up():
"""

# function for relabeling
def swap_group(molgraph,swap_rules):
    '''
    quick and dirty way to swap a 'dummy-group' in a smiles string
    with a specific functional-group
    molgraph = input molecule-graph
    swap_rules = specific rewrite-rule that swaps 'dummy-group'
                 with functional-group
    '''
    ## init a dumm-dg whose gdb contains only the input mol-graph
    ls = LabelSettings(LabelType.Term, LabelRelation.Unification)
    dg_dummy = DG(graphDatabase=[molgraph], labelSettings = ls)
    with dg_dummy.build() as b:
        ## initial subset of dg contains only the input mol-graph
        subs = [molgraph]
        ## iteratively expand the dg
        for i in range(0,2**30):
            ## apply swap_rule once on the current subset
            res= b.execute(addSubset(subs)>>swap_rules)
            ## save the resulting subset
            subs_new = res.subset
            ## check if new subset is empty, i.e. no new molecules found
            if len(subs_new) == 0:
                ## if nothing new is found stop expansion
                break
            else:
                ## else set subset to new subset and continue
                subs = subs_new
        ## last subset before expasnion ends contains only mol-graph with swaped 'dummy-groups'
        molgraph_new = subs[0]
    ## return smiles string of new mol-graph
    return molgraph_new

##############################################################
## utils for flow queries

# check which molecules of big dgs are present in a flow solution

# not sure what exactly this does
def mols_in_flow(dg, solution):
    mols_flow = []
    for v in dg.vertices:
        if solution.eval(vertex[v.graph]) != 0:
            v_graph = v.graph
        mols_flow.append(v_graph)
    print(mols_flow)
    return mols_flow


# list all edges contained in a certain flow solution with their overall flow
def edges_in_flow_solution(flow_sol, dg):
    edges_flow = {}

    for solution_index, solution in enumerate(flow_sol):
        edges_flow_x = []

        print(f"============| edges in solution {solution_index} |================")
        for e in dg.edges:
            flowOnEdge = solution.eval(edge[e])

            if flowOnEdge != 0 : 
                # print(([c.graph.name for c in e.sources],[c.graph.name for c in e.targets]),flowOnEdge)
                edge_dict = {
                    "inflow": [c.graph.name for c in e.sources],
                    "outflow": [c.graph.name for c in e.targets],
                    "flow_on_edge": flowOnEdge
                }
                print(edge_dict)
                
                edges_flow_x.append(edge_dict)

        edges_flow[f"solution_{solution_index}"] = edges_flow_x       
        print("============================")

    return edges_flow

# list all vertices contained in a certain flow solution with overall flow through them
def vertices_in_flow_solution(flow_sol, dg):
    vertices_flow = {}

    for solution_index, solution in enumerate(flow_sol):
        vertices_flow_x = []

        print(f"############| vertices in solution {solution_index} |################")
        for v in dg.vertices:
            flowOnVertex = solution.eval(vertex[v])

            if flowOnVertex != 0:
                # print(([v.graph.name], flowOnVertex))
                vertices_dict = {
                    "vertex": [v.graph.name],
                    "flow_on_vertex": flowOnVertex
                }
                # vertices_flow.append(([v.graph.name], flowOnVertex))
                print(vertices_dict)
                
                vertices_flow_x.append(vertices_dict)

        vertices_flow[f"solution_{solution_index}"] = vertices_flow_x
        print("############################")

    return vertices_flow


# save lists of dg objects as csv object
def write_csv_flow(objects_flow, output_file):
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        for obj in objects_flow:
            writer.writerow(list(obj))
            # print(str(list(obj)))
            # row = str(list(obj))
            # row.replace("\"", "")
            # row.replace("(", "")
            # row.replace(")", "")
            # print(row)
            # writer.writerow(row) 

# save dg objects as json files
def write_json_flow(objects_flow, output_file):
    with open(output_file, "w") as file:
        json.dump(objects_flow, file, indent=4)


# write ANYTHING as json
def write_json(object_dict, output_file):
    with open(output_file, "w") as file:
        json.dump(object_dict, file, indent=4)


# open ANYTHING from json
def open_json(file_name):
    with open(file_name, "r") as file:
        dictionary_or_list = json.load(file)
    return dictionary_or_list


# find the overall reaction for solutions in a flow
def find_overall_inflow_outflow(flow_solutions):

    # define a dictionary to store the solutions
    solutions_overall_reaction = {}

    # iterate over solutions in the flow.solutions
    for solution_index, solution in enumerate(flow.solutions):

        print(f"########### in and outflows in solution {solution_index} ###########")

        overall_reaction = {}
        inFlow_mols = {}
        outFlow_mols = {}

        # iterate through all vertices
        for v in dg.vertices:

            # check if a vertex has an inflow that is not zero
            inFlowVertex = solution.eval(inFlow[v])
            if inFlowVertex != 0:
                # save the name and actual inflow of the vertex
                inFlow_mols[v.graph.name] = inFlowVertex

            # check if a vertex has an outflow that is not zero
            outFlowVertex = solution.eval(outFlow[v])
            if outFlowVertex != 0:
                # save the name actual inflow of the vertex
                outFlow_mols[v.graph.name] = outFlowVertex
            
        # create an inflow dictionary containing all inflows
        overall_reaction["inflow"] = inFlow_mols
        # and an outflow dictionary containing all the outflows
        overall_reaction["outflow"] = outFlow_mols

        # save inflow and outflow for each solution in the overall dictionary
        solutions_overall_reaction[f"solution_{solution_index}"] = overall_reaction

        print(inFlow_mols)    
        print(outFlow_mols)
        # print(solutions_overall_reaction)

    return solutions_overall_reaction


# make dg graphs from flow solutions
def dg_from_flow(dg, flow_solution):
    dg_vertices_list = [v.graph for v in dg.vertices]
    dg1 = DG(graphDatabase=dg_vertices_list)
    with dg1.build() as b:
        for e in dg.edges:
            if solution.eval(edge[e]) != 0 :
                for rl in e.rules: 
                    d = Derivation()
                    d.left = list(src.graph for src in e.sources)
                    d.rule = rl
                    d.right = list(tar.graph for tar in e.targets)
                    b.addDerivation(d)
    dg1.print()
    return dg1

# get rules used in a flow solution
# NEEDS WORK, NOT WORKING YET
def rules_from_flow(dg, flow_solution):
    dg_vertices_list = [v.graph for v in dg.vertices]
    rules_used = []
    for e in dg.edges:
        if solution.eval(edge[e]) != 0 :
            # for g in e.sources:
            rules_used.append(e.graph.getGMLString())
    return rules_used

##############################################################
## utils for Energy calculations


# update the all energies database to contain only the names and not linear encoding
def convertEnergyDB():
    energies_all = energies # energies is the look up table with ALL molecules (known and unknwon) and energy of formation
    look_up_energies_all_names = {}

    for key in energies_all:
        # check if the keys are names, aka energies are in known mols or helpermols
        if key in energies_known:
            look_up_energies_all_names[key] = energies_all[key] # add the known molecules as is to the new dictionary
            continue
        
        # otherwise replace the key in the energies dictionary with the name
        else:
            oldkey_linenc = key # save the linear encoding we are trying to replace
            unknown_translation = unknown_translation_dict # the unknown names dictionary
            linenc_unknown = unknown_translation.keys() # save the linear encoding from translation dictionary
            
            for id in unknown_translation: 
                
                if oldkey_linenc == id: #linenc:
                    name_mol = unknown_translation[key] 
                    
                    look_up_energies_all_names[name_mol] = energies_all[key]
                    

    print(look_up_energies_all_names)

    write_json(look_up_energies_all_names, "new_look_up_energies_all_names.json")
    
    return look_up_energies_all_names

# calculate total dG of a solution from a list of solutions with inflows and outflows
def calculate_dG_overall(solutions_overall_inflow_outflow, energy_dictionary, output_directory):
    # define the solution dictionary to calculate the dG for all solutions of a query
    dG_solutions = {}

    # iterate through solutions
    for solution_index, solution in enumerate(solutions_overall_inflow_outflow):
        print(f"============= calculate dG for solution_{solution_index} =============")
        print(solutions_overall_inflow_outflow[solution])
        
        # to iterate over next level of dictionary, define the solution_x as the working dict
        solution_x = solutions_overall_inflow_outflow[solution]

        # set the energy counter to 0 for every solution we investigate
        energy_reactants = 0
        energy_products = 0

        # iterate through the flows, then devide between in and out flow
        for flow in solution_x:    
            print(flow)

            # to iterate over next level of dictionary, define flow_x as the working dict
            flow_x = solution_x[flow]

            # first work on the inflow
            if flow == "inflow":
                # go through inflows and find the energy 
                for mol in flow_x:

                    # find molecule in energy dictionary
                    energy_all = energy_dictionary[mol]
                    energy = energy_all[0]

                    # multiply energy times flow
                    multiplier = int(flow_x[mol])
                    flow_energy = energy * multiplier

                    # add energy to reactants
                    energy_reactants += flow_energy

            # now filter for the outflow
            if flow == "outflow":
                # go through outflows and find the energy 
                for mol in flow_x:
                    
                    # find molecule in energy dictionary
                    energy_all = energy_dictionary[mol]
                    energy = energy_all[0]

                    # multiply energy times flow
                    multiplier = int(flow_x[mol])
                    flow_energy = energy * multiplier

                    # add energy to products
                    energy_products += flow_energy

            # for quality control, print the total energies of reactants and total energy of products
            if flow == "inflow":
                print(energy_reactants)
            if flow == "outflow":
                print(energy_products)

            # calculate total dG of current solution by substracting the energy of the reactants from the energy of the products
            dG_total = energy_products - energy_reactants

            print(f"## dG total of solution_{solution_index} ##")
            print(dG_total)

            # save solution energy with its index
            dG_solutions[f"solution_{solution_index}"] = dG_total

    # write json
    write_json(dG_solutions, f"{output_directory}/energy_flow_{flow_query}_dg_{dg_id}.json")
    
    return dG_solutions


# calculate total dG of a solution WITHOUT COFACTORS from a list of solutions with inflows and outflows
def calculate_dG_overall_noATP(solutions_overall_inflow_outflow, energy_dictionary, output_directory):
    # define the solution dictionary to calculate the dG for all solutions of a query
    dG_solutions = {}

    energy_cofactors = ["ATP", "ADP", "AMP", "PPi", "Pi"]
    redox_cofactors = ["Fdox", "Fdred", "NAD+", "NADH", "NADP+", "NADPH"]

    # iterate through solutions
    for solution_index, solution in enumerate(solutions_overall_inflow_outflow):
        print(f"============= calculate dG for solution_{solution_index} =============")
        print(solutions_overall_inflow_outflow[solution])
        
        # to iterate over next level of dictionary, define the solution_x as the working dict
        solution_x = solutions_overall_inflow_outflow[solution]

        # set the energy counter to 0 for every solution we investigate
        energy_reactants = 0
        energy_products = 0

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
                        continue
                    
                    elif mol in redox_cofactors:
                        continue

                    else:
                        # find molecule in energy dictionary
                        energy_all = energy_dictionary[mol]
                        energy = energy_all[0]

                        # multiply energy times flow
                        multiplier = int(flow_x[mol])
                        flow_energy = energy * multiplier

                        # add energy to reactants
                        energy_reactants += flow_energy

            # now filter for the outflow
            if flow == "outflow":
                # go through outflows and find the energy 
                for mol in flow_x:


                    ## check if ATP, ADP, AMP, PPi, Pi
                    if mol in energy_cofactors:
                        continue

                    elif mol in redox_cofactors:
                        continue
                    
                    else:
                        # find molecule in energy dictionary
                        energy_all = energy_dictionary[mol]
                        energy = energy_all[0]

                        # multiply energy times flow
                        multiplier = int(flow_x[mol])
                        flow_energy = energy * multiplier

                        # add energy to products
                        energy_products += flow_energy

            # for quality control, print the total energies of reactants and total energy of products
            if flow == "inflow":
                print(energy_reactants)
            if flow == "outflow":
                print(energy_products)

            # calculate total dG of current solution by substracting the energy of the reactants from the energy of the products
            dG_total = energy_products - energy_reactants

            print(f"## dG total of solution_{solution_index} ##")
            print(dG_total)

            # save solution energy with its index
            dG_solutions[f"solution_{solution_index}"] = dG_total

    # write json
    write_json(dG_solutions, f"{output_directory}/energy_flow_{flow_query}_dg_{dg_id}_noATP.json")
    
    return dG_solutions