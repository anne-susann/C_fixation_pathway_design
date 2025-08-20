rule [
    ruleID "CETCH_carboxylation_ccr_carboxylase/reductase_01"
    labelType "term"
    left [
        edge [ source 0 target 2 label "=" ]
        edge [ source 9 target 10 label "-" ]
        edge [ source 11 target 13 label "=" ]
        node [ id 9 label "NADP" ] 
        node [ id 14 label "H+" ]        
    ]
    context [
        node [ id 0 label "C" ]
        node [ id 1 label "H" ]
        node [ id 2 label "C" ]
        node [ id 3 label "_X" ]
        node [ id 4 label "H" ]
        node [ id 5 label "C" ]
        node [ id 6 label "O" ]
        node [ id 7 label "S" ]
        node [ id 8 label "CoA" ]
        node [ id 10 label "H" ]
        node [ id 11 label "C" ]
        node [ id 12 label "O" ]
        node [ id 13 label "O" ]
        edge [ source 0 target 1 label "-" ]
        edge [ source 0 target 3 label "-" ]
        edge [ source 2 target 4 label "-" ]
        edge [ source 2 target 5 label "-" ]
        edge [ source 5 target 6 label "=" ]
        edge [ source 5 target 7 label "-" ]
        edge [ source 7 target 8 label "-" ]
        edge [ source 11 target 12 label "=" ]

    ]
    right [
        edge [ source 0 target 2 label "-" ]
        edge [ source 0 target 10 label "-" ]
        edge [ source 2 target 11 label "-" ]
        edge [ source 11 target 13 label "-" ]
        edge [ source 13 target 14 label "-" ]
        node [ id 9 label "NADP+" ] 
        node [ id 14 label "H" ]
    ]
    constrainLabelAny [
        label "_X"
        labels [ label "C" label "H" ]
    ]
]