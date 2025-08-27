# Carbon fixation pathway design
This repository contains the supplementary information for the results presented in the paper "Computational Approaches in Chemical Space Exploration for Carbon Fixation Pathways". This includes Python scripts and input data.

## How to run the code
1. To expand the space, the expansion script is run using mod -f all_pathways_expand.py, which loads in the grammar and utils file and saves a dg.
2. If you want to change the space expansion, make those changes in the expansion script directly.
3. To run a flow query, the query script is run using mod -f flow_query_run.py, which loads in the grammar, utils, and strategy file as well as the dg, and saves a flow file.
4. If you want to make changes to the objective function or constraints, or change the ILP solver, make these changes in the strategy file.
5. For printing a flow query, change the print_flowQuery variable to True in the flow_query_run.py script, but use this option only for small queries.
