rule [
    ruleID "3HP4HB_oxidation_3-hydroxybutyryl-CoA_dehydrogenase_01"
    labelType "term"
    left [
        edge [ source 0 target 2 label "-" ]
        edge [ source 0 target 3 label "-" ]
        edge [ source 3 target 4 label "-" ]
        node [ id 12 label "NAD+" ]    
        node [ id 4 label "H" ]

    ]
    context [
        node [ id 0 label "C" ]
        node [ id 1 label "_X" ]
        node [ id 2 label "H" ]
        node [ id 3 label "O" ]
        node [ id 5 label "C" ]
        node [ id 6 label "H" ]
        node [ id 7 label "H" ]
        node [ id 8 label "C" ]
        node [ id 9 label "O" ]
        node [ id 10 label "S" ]
        node [ id 11 label "CoA" ]
        edge [ source 0 target 1 label "-" ]
        edge [ source 0 target 5 label "-" ]
        edge [ source 5 target 6 label "-" ]
        edge [ source 5 target 7 label "-" ]
        edge [ source 5 target 8 label "-" ]
        edge [ source 8 target 9 label "=" ]
        edge [ source 8 target 10 label "-" ]
        edge [ source 10 target 11 label "-" ]        
    ]
    right [
        edge [ source 0 target 3 label "=" ]
        edge [ source 2 target 12 label "-" ]        
        node [ id 12 label "NAD" ]    
        node [ id 4 label "H+" ]
    ]
    constrainLabelAny [
        label "_X"
        labels [ label "C" label "H" ]        
    ]
]