rule [
    ruleID "CETCH_oxidation_propionyl-CoA/methylsuccinyl-CoA_oxidase_01"
    labelType "term"
    left [
        edge [ source 0 target 2 label "-" ]
        edge [ source 0 target 3 label "-" ]
        edge [ source 2 target 7 label "-" ]
        edge [ source 11 target 12 label "=" ]
    ]
    context [
        node [ id 0 label "C" ]
        node [ id 1 label "H" ]
        node [ id 2 label "C" ]
        node [ id 3 label "H" ]
        node [ id 4 label "_X" ]
        node [ id 5 label "_Y" ]
        node [ id 6 label "C" ]
        node [ id 7 label "H" ]
        node [ id 8 label "O" ]
        node [ id 9 label "S" ]
        node [ id 10 label "CoA" ]
        node [ id 11 label "O" ]
        node [ id 12 label "O" ]
        edge [ source 0 target 1 label "-" ]
        edge [ source 0 target 4 label "-" ]
        edge [ source 2 target 5 label "-" ]
        edge [ source 2 target 6 label "-" ]
        edge [ source 6 target 8 label "=" ]
        edge [ source 6 target 9 label "-" ]
        edge [ source 9 target 10 label "-" ]
    ]
    right [
        edge [ source 0 target 2 label "=" ]
        edge [ source 3 target 11 label "-" ]
        edge [ source 7 target 12 label "-" ]
        edge [ source 11 target 12 label "-" ]
    ]
    constrainLabelAny [
        label "_X"
        labels [ label "C" label "H" ]
    ]
    constrainLabelAny [
        label "_Y"
        labels [ label "C" label "H" ]
    ]
]