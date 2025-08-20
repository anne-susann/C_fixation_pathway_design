rule [
    ruleID "CETCH_rearrangement_ethylmalonyl-CoA_mutase_02"
    labelType "term"
    left [
        edge [ source 0 target 2 label "-" ]
        edge [ source 3 target 10 label "-" ]
    ]
    context [
        node [ id 0 label "C" ]
        node [ id 1 label "H" ]
        node [ id 2 label "C" ]
        node [ id 3 label "C" ]
        node [ id 4 label "C" ]
        node [ id 5 label "O" ]
        node [ id 6 label "O" ]
        node [ id 7 label "H" ]
        node [ id 8 label "H" ]
        node [ id 9 label "H" ]
        node [ id 10 label "_X" ]
        node [ id 11 label "O" ]
        node [ id 12 label "S" ]
        node [ id 13 label "CoA" ]
        edge [ source 0 target 1 label "-" ]
        edge [ source 0 target 3 label "-" ]
        edge [ source 0 target 4 label "-" ]
        edge [ source 2 target 5 label "=" ]
        edge [ source 2 target 6 label "-" ]
        edge [ source 6 target 7 label "-" ]
        edge [ source 4 target 11 label "=" ]
        edge [ source 4 target 12 label "-" ]
        edge [ source 12 target 13 label "-" ]
        edge [ source 3 target 8 label "-" ]
        edge [ source 3 target 9 label "-" ]
    ]
    right [
        edge [ source 0 target 10 label "-" ]
        edge [ source 2 target 3 label "-" ]
    ]
    constrainLabelAny [
        label "_X"
        labels [ label "C" label "H" ]
    ]
]