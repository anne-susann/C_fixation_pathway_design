rule [
    ruleID "CBB_ribulose-5-P_epimerase"
    labelType "term"
    left [
        node [ id 1 label "xyO" ]
    ]
    context [
        node [ id 0 label "C" ]
        node [ id 2 label "H" ]
        edge [ source 0 target 1 label "-" ]
        edge [ source 1 target 2 label "-" ]
    ]
    right [
        node [ id 1 label "O" ]
    ]
]