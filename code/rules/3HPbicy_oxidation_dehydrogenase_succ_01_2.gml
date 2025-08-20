rule [
    ruleID "3HPbicy_oxidation_succinate_dehydrogenase_01_2"
    labelType "term"
    left [
        edge [ source 0 target 1 label "-" ]
        edge [ source 0 target 3 label "-" ]
        edge [ source 1 target 2 label "-" ]
        edge [ source 14 target 15 label "=" ]
        edge [ source 14 target 16 label "=" ]        
    ]
    context [
        node [ id 0 label "C" ]
        node [ id 1 label "C" ]
        node [ id 2 label "H" ]
        node [ id 3 label "H" ]
        node [ id 4 label "C" ]
        node [ id 5 label "_X" ]
        node [ id 6 label "_Y" ]
        node [ id 7 label "C" ]
        node [ id 8 label "O" ]
        node [ id 9 label "O" ]
        node [ id 10 label "H" ]
        node [ id 14 label "UQ" ]
        node [ id 15 label "O" ]
        node [ id 16 label "O" ]
        edge [ source 0 target 4 label "-" ]
        edge [ source 0 target 5 label "-" ]
        edge [ source 1 target 6 label "-" ]
        edge [ source 1 target 7 label "-" ]
        edge [ source 7 target 8 label "=" ]
        edge [ source 7 target 9 label "-" ]
        edge [ source 9 target 10 label "-" ]        
    ]
    right [
        edge [ source 0 target 1 label "=" ]
        edge [ source 3 target 16 label "-" ]
        edge [ source 2 target 15 label "-" ]
        edge [ source 14 target 15 label "-" ]
        edge [ source 14 target 16 label "-" ]
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