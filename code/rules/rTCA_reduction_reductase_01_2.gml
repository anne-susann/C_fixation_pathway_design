rule [
    ruleID "rTCA_reduction_fumarate_reductase_01_2"
    labelType "term"
    left [
        edge [ source 0 target 2 label "=" ]
        edge [ source 13 target 14 label "-" ]
        node [ id 12 label "H+" ]
        node [ id 13 label "NAD" ]
    ]
    context [
        node [ id 0 label "C" ]
        node [ id 1 label "_X" ]
        node [ id 2 label "C" ]
        node [ id 3 label "C" ]
        node [ id 4 label "_Y" ]
        node [ id 5 label "C" ]
        node [ id 6 label "O" ]
        node [ id 7 label "O" ]
        node [ id 10 label "H" ]
        node [ id 14 label "H" ]
        edge [ source 0 target 1 label "-" ]
        edge [ source 0 target 3 label "-" ]
        edge [ source 3 target 7 label "=" ]
        edge [ source 3 target 6 label "-" ]
        edge [ source 6 target 10 label "-" ]
        edge [ source 2 target 4 label "-" ]
        edge [ source 2 target 5 label "-" ]        
    ]
    right [
        edge [ source 0 target 2 label "-" ]
        edge [ source 0 target 12 label "-" ]
        edge [ source 2 target 14 label "-" ]
        node [ id 12 label "H" ]
        node [ id 13 label "NAD+" ]
    ]
    constrainLabelAny [
        label "_X"
        labels [ label "H" label "C" ]        
    ]
    constrainLabelAny [
        label "_Y"
        labels [ label "H" label "C" ]        
    ]
]