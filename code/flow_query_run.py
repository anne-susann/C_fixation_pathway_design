# ASABEL
# perform flow queries

# input in command line as: mod -f all_pathways_expansion.py

############## import #################
## import functions
include("utils/functions_co2_01.py")

## import grammar scripts used for dg creation
include("grammars/all_grammar_2.py")



## define dg to be loaded
dg_id = "gly_ala_2_2"

## load dg
dg = DG.load(inputGraphs, rset, f"dg_dump/all_pathways_noCBB_{dg_id}.dg") 

## output directory
output_dir = "1000_sol"

## check loaded dg
display_size_dg(dg)
# print(helpermols)


############## flow query #################

## define flow query 
flow_query = "1_ac_enumerate_1000"

start_flowQuery = True

print_flowQuery = False

if start_flowQuery == True:
    print("############## flow query #################")

    # find specific pathway

    include(f'strategies/all_flowq_{flow_query}.py')

    # dump solutions
    flow.dump(f"1000_sol/all_flowq_{flow_query}_grammar_2_{dg_id}.flow")

    # examine the flow solutions
    edges_flow = edges_in_flow_solution(flow.solutions, dg)
    vertices_flow = vertices_in_flow_solution(flow.solutions, dg)
   
    ## write file to create step by step dg
   
    ### for JSON file
    write_json_flow(edges_flow, f"{output_dir}/edges_flowq_{flow_query}_solutions_{dg_id}.json")
    write_json_flow(vertices_flow, f"{output_dir}/vertices_flowq_{flow_query}_solutions_{dg_id}.json")

    # save the inflow and outflows separately for post-annotation
    overall_reactions = find_overall_inflow_outflow(flow.solutions)
    print(overall_reactions)
    write_json(overall_reactions, f"{output_dir}/overall_reactions_{dg_id}_{flow_query}.json")



    if print_flowQuery == True:
        flowPrinter = hyperflow.Printer()
        flowPrinter.printUnfiltered = False
        # flowPrinter.dgPrinter.withRuleId = False
        for s in flow.solutions:
        	flowPrinter.dgPrinter.pushVertexVisible(lambda v: not is_in_graphlist(v.graph, helpermols))
            s.print(flowPrinter)



    # print rules used for dg creation
    # print_input_rules()
   
    


    
    # flow.solutions.print()

###############################
## PetriNet


start_petriNet = False

if start_petriNet == True:
    print("############## petri Net #################")
    include("strategies/petriNet.py")
