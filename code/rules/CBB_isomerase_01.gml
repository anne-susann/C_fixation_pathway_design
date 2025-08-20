rule [
    ruleID "CBB_ribose-5-P_isomerase_01"
    labelType "term"
    left [
        edge [ source 0 target 3 label "=" ]
        edge [ source 1 target 5 label "-" ]
        edge [ source 1 target 6 label "-" ]
        edge [ source 6 target 7 label "-" ]
    ]
    context [
        node [ id 0 label "C" ]
        node [ id 1 label "C" ]
        node [ id 2 label "C" ]
        node [ id 3 label "O" ]
        node [ id 4 label "H" ]
        node [ id 5 label "H" ]
        node [ id 6 label "O" ]
        node [ id 7 label "H" ]
        edge [ source 0 target 4 label "-" ]
        edge [ source 0 target 1 label "-" ]
        edge [ source 1 target 2 label "-" ]        
    ]
    right [
        edge [ source 0 target 3 label "-" ]
        edge [ source 0 target 5 label "-" ]
        edge [ source 3 target 7 label "-" ]
        edge [ source 1 target 6 label "=" ]
    ]
]