rule [
    ruleID "GLYOX_activation_malate_synthase_a_01"
    labelType "term"
    left [
        edge [ source 0 target 1 label "=" ]
        edge [ source 6 target 7 label "-" ]
    ]
    context [
        node [ id 0 label "C" ]
        node [ id 1 label "O" ]
        node [ id 2 label "H" ]
        node [ id 3 label "C" ]
        node [ id 4 label "O" ]
        node [ id 5 label "_X" ]
        node [ id 6 label "C" ]
        node [ id 7 label "H" ]
        node [ id 8 label "_Y" ]
        node [ id 9 label "H" ]
        node [ id 10 label "C" ]
        node [ id 11 label "O" ]
        node [ id 12 label "S" ]
        edge [ source 0 target 2 label "-" ]
        edge [ source 0 target 3 label "-" ]
        edge [ source 3 target 4 label "=" ]
        edge [ source 3 target 5 label "-" ]
        edge [ source 6 target 8 label "-" ]
        edge [ source 6 target 9 label "-" ]
        edge [ source 6 target 10 label "-" ]
        edge [ source 10 target 11 label "=" ]        
        edge [ source 10 target 12 label "-" ]
    ]
    right [
        edge [ source 0 target 1 label "-" ]        
        edge [ source 1 target 7 label "-" ]
        edge [ source 0 target 6 label "-" ]        
    ]
    constrainLabelAny [
        label "_X"
        labels [ label "O" label "S" ]
    ]
    constrainLabelAny [
        label "_Y"
        labels [ label "C" label "H" ]
    ]
]