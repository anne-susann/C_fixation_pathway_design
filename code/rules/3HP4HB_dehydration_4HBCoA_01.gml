rule [
    ruleID "3HP4HB_dehydration_4HBCoA_dehydratase_01"
    labelType "term"
    left [
        edge [ source 0 target 3 label "-" ]
        edge [ source 0 target 4 label "-" ]
        edge [ source 2 target 6 label "-" ]
        edge [ source 4 target 9 label "-" ]
    ]
    context [
        node [ id 0 label "C" ]
        node [ id 1 label "H" ]
        node [ id 2 label "C" ]
        node [ id 3 label "H" ]
        node [ id 4 label "C" ]
        node [ id 5 label "H" ]
        node [ id 6 label "O" ]
        node [ id 7 label "H" ]
        node [ id 8 label "H" ]
        node [ id 9 label "H" ]
        node [ id 10 label "_X" ]
        node [ id 11 label "H" ]
        edge [ source 0 target 1 label "-" ]
        edge [ source 0 target 2 label "-" ]
        edge [ source 2 target 5 label "-" ]
        edge [ source 2 target 7 label "-" ]
        edge [ source 6 target 11 label "-" ]
        edge [ source 4 target 8 label "-" ]
        edge [ source 4 target 10 label "-" ]
    ]
    right [
        edge [ source 0 target 4 label "=" ]
        edge [ source 2 target 3 label "-" ]
        edge [ source 6 target 9 label "-" ]
    ]
    constrainLabelAny [
        label "_X"
        labels [label "C" ]
    ]
]