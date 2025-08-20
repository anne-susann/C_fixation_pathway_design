rule [
    ruleID "GLYOX_alanine_2,3_aminomutase_01"
    labelType "term"
    left [
        edge [ source 0 target 3 label "-" ]
        edge [ source 1 target 5 label "-" ]
    ]
    context [
        node [ id 0 label "C" ]
        node [ id 1 label "C" ]
        node [ id 2 label "C" ]
        node [ id 3 label "N" ]
        node [ id 4 label "O" ]
        node [ id 5 label "H" ]
        edge [ source 0 target 1 label "-" ]
        edge [ source 1 target 2 label "-" ]
        edge [ source 2 target 4 label "=" ]      
    ]
    right [
        edge [ source 1 target 3 label "-" ]
        edge [ source 0 target 5 label "-" ]
    ]
]