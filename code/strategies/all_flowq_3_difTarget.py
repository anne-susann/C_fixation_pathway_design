# ASABEL
# flow query to use for finding pathway in the CO2 chemical space

###############################
# find different flow queries 

# setup integer hyperflow problem
flow = hyperflow.Model(dg)
# flow = Flow(dg)


# speficy which molecules can flow into the cycle
flow.addSource(propCoA)


for mol in helpermols:
    flow.addSource(mol)

# specify which molecules can remain in the network

flow.addSink(propCoA)


for mol in helpermols:
    flow.addSink(mol)

## specify restrictions
# enable constraint for autocatalysis
flow.overallAutocatalysis.enable()

# flow.addConstraint(inFlow[acCoA] == 1)
flow.addConstraint(outFlow[propCoA] == 2)
# flow.addConstraint(vertex[citrate] == 0)
# flow.addConstraint(vertex[oxala] == 0)
# flow.addConstraint(vertex[HB4] == 0)



# Specify the minimization criteria:
#  number of unique reactions used
flow.objectiveFunction = isEdgeUsed
# flow.objectiveFunction = edge + inFlow


## solve ILP 
flow.findSolutions(maxNumSolutions = 100)
# flow.findSolutions()
flow.solutions.list()

flowPrinter = hyperflow.Printer()
flowPrinter.printUnfiltered = False
# flowPrinter.dgPrinter.withRuleId = False
for s in flow.solutions:
	flowPrinter.dgPrinter.pushVertexVisible(lambda v: not is_in_graphlist(v.graph, helpermols))
	s.print(flowPrinter)


# flow.solutions.print()

# print(mols_in_flow(dg, flow.solutions))