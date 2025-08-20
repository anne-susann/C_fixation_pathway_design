rule [
    ruleID "rTCA_reduction_malate_dehydrogenase_01"
    labelType "term"
    left [
        edge [ source 0 target 1 label "=" ]
        edge [ source 10 target 11 label "-" ]
        node [ id 10 label "NADP" ]    
        node [ id 12 label "H+" ]
    ]
    context [
        node [ id 0 label "C" ]
        node [ id 1 label "O" ]
        node [ id 2 label "C" ]
        node [ id 3 label "O" ]
        node [ id 4 label "C" ]
        node [ id 5 label "_X" ]
        node [ id 6 label "_Z" ]
        node [ id 7 label "_Y" ]
        node [ id 8 label "O" ]
        node [ id 9 label "H" ]
        node [ id 11 label "H" ]
        edge [ source 0 target 2 label "-" ]
        edge [ source 0 target 4 label "-" ]
        edge [ source 4 target 5 label "-" ]
        edge [ source 4 target 6 label "-" ]
        edge [ source 4 target 7 label "-" ]
        edge [ source 2 target 3 label "=" ]
        edge [ source 2 target 8 label "-" ]
        edge [ source 8 target 9 label "-" ]
    ]
    right [
        edge [ source 0 target 1 label "-" ]
        edge [ source 0 target 11 label "-" ]
        edge [ source 1 target 12 label "-" ]
        node [ id 10 label "NADP+" ]       
        node [ id 12 label "H" ]
    ]
    constrainLabelAny [
        label "_X"
        labels [ label "C" label "H" ]
    ]
    constrainLabelAny [
        label "_Y"
        labels [ label "C" label "H" ]
    ]
    constrainLabelAny [
        label "_Z"
        labels [ label "C" label "H" ]
    ]
]