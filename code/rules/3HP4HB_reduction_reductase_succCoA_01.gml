rule [
    ruleID "3HP4HB_reduction_succinyl-CoA_reductase_01"
    labelType "term"
    left [
        edge [ source 0 target 1 label "-" ]
        edge [ source 8 target 9 label "-" ]        
        node [ id 9 label "NADP" ]
        node [ id 10 label "H+" ]
    ]
    context [
        node [ id 0 label "C" ]
        node [ id 1 label "S" ]
        node [ id 2 label "CoA" ]
        node [ id 3 label "O" ]
        node [ id 4 label "C" ]
        node [ id 5 label "H" ]
        node [ id 6 label "H" ]
        node [ id 7 label "_X" ]
        node [ id 8 label "H" ]
        edge [ source 0 target 3 label "=" ]
        edge [ source 1 target 2 label "-" ]
        edge [ source 0 target 4 label "-" ]       
        edge [ source 4 target 5 label "-" ]
        edge [ source 4 target 6 label "-" ]
        edge [ source 4 target 7 label "-" ]        
    ]
    right [
        edge [ source 0 target 8 label "-" ]
        edge [ source 1 target 10 label "-" ]
        node [ id 9 label "NADP+" ]
        node [ id 10 label "H" ]
    ]
    constrainLabelAny [
        label "_X"
        labels [ label "C" ]        
    ]
]