rule [
    ruleID "GLYOX_lysis_isocitrate_lyase_01"
    labelType "term"
    left [
        edge [ source 0 target 6 label "-" ]
        edge [ source 6 target 9 label "-" ]
        edge [ source 9 target 10 label "-" ]
    ]
    context [
        node [ id 0 label "C" ]
        node [ id 1 label "C" ]
        node [ id 2 label "O" ]
        node [ id 3 label "O" ]
        node [ id 4 label "_X" ]
        node [ id 5 label "H" ]
        node [ id 6 label "C" ]
        node [ id 7 label "H" ]
        node [ id 8 label "C" ]
        node [ id 9 label "O" ]
        node [ id 10 label "H" ]
        node [ id 11 label "O" ]
        node [ id 12 label "O" ]
        edge [ source 0 target 1 label "-" ]
        edge [ source 1 target 2 label "=" ]
        edge [ source 1 target 3 label "-" ]
        edge [ source 0 target 4 label "-" ]
        edge [ source 0 target 5 label "-" ]
        edge [ source 6 target 7 label "-" ]
        edge [ source 6 target 8 label "-" ]
        edge [ source 8 target 11 label "=" ]
        edge [ source 8 target 12 label "-" ]                
    ]
    right [
        edge [ source 0 target 10 label "-" ]
        edge [ source 6 target 9 label "=" ]
    ]
      constrainLabelAny [
        label "_X"
        labels [ label "H" label "C" ]        
    ]
]