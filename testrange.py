import scipy

#Radius
OuterRadius = 0.0125
InnerRadius = 0.0005

#Simulated coordinates
SolundirLAT = 60.979406
SolundirLON = 5.077910


#Mjomna

MjomnaOuterLAT1 = 60.918404 - OuterRadius
MjomnaOuterLON1 = 4.901205 - OuterRadius
MjomnaOuterLAT2 = 60.918404 + OuterRadius
MjomnaOuterLON2 = 4.901205 + OuterRadius

MjomnaInnerLAT1 = 60.918404 - InnerRadius
MjomnaInnerLON1 = 4.901205 - InnerRadius
MjomnaInnerLAT2 = 60.918404 + OuterRadius
MjomnaInnerLON2 = 4.901205 + OuterRadius

MjomnaOuterRingLAT = scipy.arange(MjomnaOuterLAT1, MjomnaOuterLAT2, 0.000001)
MjomnaOuterRingLAT = scipy.around(MjomnaOuterRingLAT, 6)

MjomnaOuterRingLON = scipy.arange(MjomnaOuterLON1, MjomnaOuterLON2, 0.000001)
MjomnaOuterRingLON = scipy.around(MjomnaOuterRingLON, 6)

if SolundirLAT in MjomnaOuterRingLAT and SolundirLON in MjomnaOuterRingLON:
    print('Solundir is in outer ring in Mjomna')

MjomnaInnerRingLAT = scipy.arange(MjomnaInnerLAT1, MjomnaInnerLAT2, 0.000001)
MjomnaInnerRingLAT = scipy.around(MjomnaInnerRingLAT, 6)

MjomnaInnerRingLON = scipy.arange(MjomnaInnerLON1, MjomnaInnerLON2, 0.000001)
MjomnaInnerRingLON = scipy.around(MjomnaInnerRingLON, 6)

if SolundirLAT in MjomnaInnerRingLAT and SolundirLON in MjomnaInnerRingLON:
    print('Solundir is in inner ring in Mjomna')

#################################################################################
#Eivindvik

EivindvikOuterLAT1 = 60.979406 - OuterRadius
EivindvikOuterLON1 = 5.077910 - OuterRadius
EivindvikOuterLAT2 = 60.979406 + OuterRadius
EivindvikOuterLON2 = 5.077910 + OuterRadius

EivindvikInnerLAT1 = 60.979406 - InnerRadius
EivindvikInnerLON1 = 5.077910 - InnerRadius
EivindvikInnerLAT2 = 60.979406 + OuterRadius
EivindvikInnerLON2 = 5.077910 + OuterRadius

EivindvikOuterRingLAT = scipy.arange(EivindvikOuterLAT1, EivindvikOuterLAT2, 0.000001)
EivindvikOuterRingLAT = scipy.around(EivindvikOuterRingLAT, 6)

EivindvikOuterRingLON = scipy.arange(EivindvikOuterLON1, EivindvikOuterLON2, 0.000001)
EivindvikOuterRingLON = scipy.around(EivindvikOuterRingLON, 6)

if SolundirLAT in EivindvikOuterRingLAT and SolundirLON in EivindvikOuterRingLON:
    print('Solundir is in outer ring in Eivindvik')

EivindvikInnerRingLAT = scipy.arange(EivindvikInnerLAT1, EivindvikInnerLAT2, 0.000001)
EivindvikInnerRingLAT = scipy.around(EivindvikInnerRingLAT, 6)

EivindvikInnerRingLON = scipy.arange(EivindvikInnerLON1, EivindvikInnerLON2, 0.000001)
EivindvikInnerRingLON = scipy.around(EivindvikInnerRingLON, 6)

if SolundirLAT in EivindvikInnerRingLAT and SolundirLON in EivindvikInnerRingLON:
    print('Solundir is in inner ring in Eivindvik')

#####################################################################################