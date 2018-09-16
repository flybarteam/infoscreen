import scipy


OuterRadius = 0.0125
InnerRadius = 0.0005

SolundirLAT = 60.918408
SolundirLON = 4.901205

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
    print('Solundir er i ytre ring')

MjomnaInnerRingLAT = scipy.arange(MjomnaInnerLAT1, MjomnaInnerLAT2, 0.000001)
MjomnaInnerRingLAT = scipy.around(MjomnaInnerRingLAT, 6)

MjomnaInnerRingLON = scipy.arange(MjomnaInnerLON1, MjomnaInnerLON2, 0.000001)
MjomnaInnerRingLON = scipy.around(MjomnaInnerRingLON, 6)

if SolundirLAT in MjomnaInnerRingLAT and SolundirLON in MjomnaInnerRingLON:
    print('Solundir er i indre ring')