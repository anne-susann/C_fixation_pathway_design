rule [
    ruleID "3HP4HB_reduction_3-hydroxypropionate_dehydrogenase_01"
    labelType "term"
    left [
        edge [ source 0 target 1 label "=" ]
        edge [ source 7 target 8 label "-" ]
        node [ id 7 label "NADP" ]    
        node [ id 9 label "H+" ]
    ]
    context [
        node [ id 0 label "C" ]
        node [ id 1 label "O" ]
        node [ id 2 label "H" ]
        node [ id 3 label "C" ]
        node [ id 4 label "_X" ]
        node [ id 5 label "_Z" ]
        node [ id 6 label "_Y" ]
        node [ id 8 label "H" ]
        edge [ source 0 target 2 label "-" ]
        edge [ source 0 target 3 label "-" ]
        edge [ source 3 target 4 label "-" ]
        edge [ source 3 target 5 label "-" ]
        edge [ source 3 target 6 label "-" ]
    ]
    right [
        edge [ source 0 target 1 label "-" ]
        edge [ source 0 target 8 label "-" ]
        edge [ source 1 target 9 label "-" ]
        node [ id 7 label "NADP+" ]       
        node [ id 9 label "H" ]
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