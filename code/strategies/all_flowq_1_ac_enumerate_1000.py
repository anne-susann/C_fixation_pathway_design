# ASABEL
# flow query to use for finding pathway in the CO2 chemical space

###############################
# find autocatalytic cycle 

# only if run alone
# include("utils/functions_co2_01.py")

# setup integer hyperflow problem
flow = hyperflow.Model(dg)
# flow = hyperflow.Model(dg, ilpSolver = "CPLEX")

# speficy which molecules can flow into the cycle
flow.addSource(acCoA)

for mol in helpermols:
    flow.addSource(mol)

# for mol in eductmols:
#     flow.addSource(mol)

# specify which molecules can remain in the network
flow.addSink(acCoA)

for mol in helpermols:
    flow.addSink(mol)

# for mol in eductmols:
#     flow.addSink(mol)

## specify restrictions
# enable constraint for autocatalysis
flow.overallAutocatalysis.enable()
flow.allowIOReversal = False

# flow.addConstraint(inFlow[acCoA] == 1)
flow.addConstraint(outFlow[acCoA] == 2)

# enumerate
flow.addEnumerationVar(isEdgeUsed)


# Specify the minimization criteria:
#  number of unique reactions used
# flow.objectiveFunction = isEdgeUsed
flow.objectiveFunction = isEdgeUsed * 1000 + edgeFlow
# flow.objectiveFunction = edgeFlow


## solve ILP 
flow.findSolutions(maxNumSolutions = 1000)
flow.solutions.list()

## print flow in summary



# flowPrinter = FlowPrinter(hide_mols)
# dgprint = hide_mols(helpermols)
# # flowPrinter.printUnfiltered = True
# flow.solutions.print(dgprint)



# flow.solutions.print()