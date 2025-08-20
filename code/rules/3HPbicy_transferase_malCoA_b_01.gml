rule [
    ruleID "3HPbicy_transferase_succinyl-CoA_malate-CoA_transferase_b_01"
    labelType "term"
    left [
        edge [ source 0 target 3 label "-" ]
        edge [ source 12 target 14 label "-" ]
    ]
    context [
        node [ id 0 label "C" ]
        node [ id 1 label "C" ]
        node [ id 2 label "O" ]
        node [ id 3 label "O" ]
        node [ id 4 label "H" ]
        node [ id 5 label "H" ]
        node [ id 6 label "H" ]
        node [ id 7 label "C" ]
        node [ id 8 label "_X" ]
        node [ id 9 label "H" ]
        node [ id 10 label "O" ]
        node [ id 11 label "H" ]
        node [ id 12 label "S" ]
        node [ id 13 label "CoA" ]
        node [ id 14 label "H" ]
        edge [ source 0 target 1 label "-" ]
        edge [ source 0 target 2 label "=" ]
        edge [ source 3 target 4 label "-" ]
        edge [ source 1 target 5 label "-" ]
        edge [ source 1 target 6 label "-" ]
        edge [ source 1 target 7 label "-" ]
        edge [ source 7 target 8 label "-" ]
        edge [ source 7 target 9 label "-" ]
        edge [ source 7 target 10 label "-" ]
        edge [ source 10 target 11 label "-" ]
        edge [ source 12 target 13 label "-" ]
    ]
    right [
        edge [ source 0 target 12 label "-" ]
        edge [ source 3 target 14 label "-" ]
    ]
    constrainLabelAny [
        label "_X"
        labels [ label "C" ]        
    ]
]