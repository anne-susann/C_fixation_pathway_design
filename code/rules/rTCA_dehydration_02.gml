rule [
    ruleID "rTCA_dehydration_rehydration_aconitase_02"
    labelType "term"
    left [
        edge [ source 0 target 1 label "=" ]
        edge [ source 4 target 6 label "-" ]
    ]
    context [
        node [ id 0 label "C" ]
        node [ id 1 label "C" ]
        node [ id 2 label "H" ]
        node [ id 3 label "C" ]
        node [ id 4 label "H" ]
        node [ id 5 label "_X" ]
        node [ id 6 label "O" ]
        node [ id 7 label "_Y" ]
        node [ id 8 label "O" ]
        node [ id 9 label "O" ]
        node [ id 10 label "H" ]
        node [ id 11 label "H" ]
        edge [ source 0 target 5 label "-" ]
        edge [ source 0 target 7 label "-" ]
        edge [ source 1 target 2 label "-" ]
        edge [ source 1 target 3 label "-" ]
        edge [ source 3 target 8 label "=" ]
        edge [ source 3 target 9 label "-" ]
        edge [ source 9 target 10 label "-" ]
        edge [ source 6 target 11 label "-" ]
    ]
    right [
        edge [ source 0 target 1 label "-" ]
        edge [ source 0 target 6 label "-" ]
        edge [ source 1 target 4 label "-" ]
    ]
    constrainLabelAny [
        label "_X"
        labels [ label "C" ]
    ]
    constrainLabelAny [
        label "_Y"
        labels [ label "C" ]
    ]
]