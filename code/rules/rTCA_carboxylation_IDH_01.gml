rule [
    ruleID "rTCA_carboxylation_IDH_01"
    labelType "term"
    left [
        edge [ source 0 target 4 label "-" ]
        edge [ source 2 target 6 label "=" ]
        edge [ source 10 target 12 label "=" ]
        edge [ source 13 target 14 label "-" ]
        node [ id 13 label "NADP" ]
        node [ id 15 label "H+" ]
    ]
    context [
        node [ id 0 label "C" ]
        node [ id 1 label "C" ]
        node [ id 2 label "C" ]
        node [ id 3 label "H" ]
        node [ id 4 label "H" ]
        node [ id 5 label "C" ]
        node [ id 6 label "O" ]
        node [ id 7 label "O" ]
        node [ id 8 label "O" ]
        node [ id 9 label "H" ]
        node [ id 10 label "C" ]
        node [ id 11 label "O" ]
        node [ id 12 label "O" ]
        node [ id 14 label "H" ]
        node [ id 16 label "_X" ]
        node [ id 17 label "_Y" ]
        node [ id 18 label "_Z" ]        
        edge [ source 0 target 1 label "-" ]
        edge [ source 0 target 2 label "-" ]
        edge [ source 0 target 3 label "-" ]
        edge [ source 2 target 5 label "-" ]
        edge [ source 5 target 7 label "=" ]
        edge [ source 5 target 8 label "-" ]
        edge [ source 8 target 9 label "-" ]
        edge [ source 10 target 11 label "=" ]
        edge [ source 1 target 16 label "-" ]
        edge [ source 1 target 17 label "-" ]
        edge [ source 1 target 18 label "-" ]        
    ]
    right [
        edge [ source 0 target 10 label "-" ]
        edge [ source 10 target 12 label "-" ]
        edge [ source 4 target 12 label "-" ]
        edge [ source 2 target 6 label "-" ]
        edge [ source 2 target 14 label "-" ]
        edge [ source 6 target 15 label "-" ]
        node [ id 13 label "NADP+" ]
        node [ id 15 label "H" ]
    ]
    constrainLabelAny [
        label "_X"
        labels [ label "C" label "H" ]
    ]
    constrainLabelAny [
        label "_Y"
        labels [ label "C" label "H" ]
    ]
    constrainLabelAny [
        label "_Z"
        labels [ label "C" label "H" ]
    ]
]