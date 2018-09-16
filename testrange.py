import scipy


OuterRadius = 0.0125
InnerRadius = 0.0005

SolundirLAT = 60.905908
SolundirLON = 4.901205

MjomnaOuterLAT1 = 60.918404 - OuterRadius
MjomnaOuterLON1 = 4.901205 - OuterRadius
MjomnaOuterLAT2 = 60.918404 + OuterRadius
MjomnaOuterLON2 = 4.901205 + OuterRadius

#MjomnaOuterRingLAT = np.linspace(MjomnaOuterLAT1, MjomnaOuterLAT2, 100000001)
#MjomnaOuterRingLON = np.linspace(MjomnaOuterLON1, MjomnaOuterLON2, 100000001)

MjomnaOuterRingLAT = scipy.arange(MjomnaOuterLAT1, MjomnaOuterLAT2, 0.000001)
MjomnaOuterRingLAT = scipy.around(MjomnaOuterRingLAT, 6)





if SolundirLAT in MjomnaOuterRingLAT:
    print('Solundir er i ytre ring')