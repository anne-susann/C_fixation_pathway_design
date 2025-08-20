rule [
    ruleID "3HP4HB_reduction_acrylyl-CoA_reductase_01"
    labelType "term"
    left [
        edge [ source 0 target 2 label "=" ]
        edge [ source 9 target 10 label "-" ]
        node [ id 9 label "NADP" ]
        node [ id 11 label "H+" ]
    ]
    context [
        node [ id 0 label "C" ]
        node [ id 1 label "H" ]
        node [ id 2 label "C" ]
        node [ id 3 label "C" ]
        node [ id 4 label "H" ]
        node [ id 5 label "_X" ]
        node [ id 6 label "O" ]
        node [ id 7 label "S" ]
        node [ id 8 label "CoA" ]
        node [ id 10 label "H" ]
        edge [ source 0 target 1 label "-" ]
        edge [ source 0 target 3 label "-" ]
        edge [ source 3 target 6 label "=" ]
        edge [ source 3 target 7 label "-" ]
        edge [ source 7 target 8 label "-" ]
        edge [ source 2 target 4 label "-" ]
        edge [ source 2 target 5 label "-" ]        
    ]
    right [
        edge [ source 0 target 2 label "-" ]
        edge [ source 0 target 10 label "-" ]
        edge [ source 2 target 11 label "-" ]
        node [ id 9 label "NADP+" ]
        node [ id 11 label "H" ]
    ]
    constrainLabelAny [
        label "_X"
        labels [ label "C" label "H" ]
    ]
]