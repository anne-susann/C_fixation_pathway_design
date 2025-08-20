rule [
    ruleID "GLYOX_transaminase_01"
    labelType "term"
    left [
        edge [ source 0 target 1 label "=" ]
        edge [ source 5 target 6 label "-" ]
        edge [ source 5 target 7 label "-" ]
    ]
    context [
        node [ id 0 label "C" ]
        node [ id 1 label "O" ]
        node [ id 2 label "H" ]
        node [ id 3 label "C" ]
        node [ id 4 label "C" ]
        node [ id 5 label "C" ]
        node [ id 6 label "N" ]
        node [ id 7 label "H" ]
        node [ id 8 label "C" ]
        node [ id 9 label "C" ]
        edge [ source 0 target 2 label "-" ]
        edge [ source 0 target 3 label "-" ]
        edge [ source 3 target 4 label "-" ]
        edge [ source 5 target 8 label "-" ]
        edge [ source 5 target 9 label "-" ]            
    ]
    right [
        edge [ source 0 target 6 label "-" ]
        edge [ source 0 target 7 label "-" ]
        edge [ source 5 target 1 label "=" ]
    ]
]