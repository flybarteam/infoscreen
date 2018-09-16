import scipy

#Radius
OuterRadius = 0.0125
InnerRadius = 0.0005

#Simulated coordinates
SolundirLAT = 61.019066
SolundirLON = 4.741218


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
#Austrheim

AustrheimOuterLAT1 = 60.789151 - OuterRadius
AustrheimOuterLON1 = 4.939859 - OuterRadius
AustrheimOuterLAT2 = 60.789151 + OuterRadius
AustrheimOuterLON2 = 4.939859 + OuterRadius

AustrheimInnerLAT1 = 60.789151 - InnerRadius
AustrheimInnerLON1 = 4.939859 - InnerRadius
AustrheimInnerLAT2 = 60.789151 + OuterRadius
AustrheimInnerLON2 = 4.939859 + OuterRadius

AustrheimOuterRingLAT = scipy.arange(AustrheimOuterLAT1, AustrheimOuterLAT2, 0.000001)
AustrheimOuterRingLAT = scipy.around(AustrheimOuterRingLAT, 6)

AustrheimOuterRingLON = scipy.arange(AustrheimOuterLON1, AustrheimOuterLON2, 0.000001)
AustrheimOuterRingLON = scipy.around(AustrheimOuterRingLON, 6)

if SolundirLAT in AustrheimOuterRingLAT and SolundirLON in AustrheimOuterRingLON:
    print('Solundir is in outer ring in Austrheim')

AustrheimInnerRingLAT = scipy.arange(AustrheimInnerLAT1, AustrheimInnerLAT2, 0.000001)
AustrheimInnerRingLAT = scipy.around(AustrheimInnerRingLAT, 6)

AustrheimInnerRingLON = scipy.arange(AustrheimInnerLON1, AustrheimInnerLON2, 0.000001)
AustrheimInnerRingLON = scipy.around(AustrheimInnerRingLON, 6)

if SolundirLAT in AustrheimInnerRingLAT and SolundirLON in AustrheimInnerRingLON:
    print('Solundir is in inner ring in Austrheim')

###########################################################################
#Nara

NaraOuterLAT1 = 61.019066 - OuterRadius
NaraOuterLON1 = 4.741218 - OuterRadius
NaraOuterLAT2 = 61.019066 + OuterRadius
NaraOuterLON2 = 4.741218 + OuterRadius

NaraInnerLAT1 = 61.019066 - InnerRadius
NaraInnerLON1 = 4.741218 - InnerRadius
NaraInnerLAT2 = 61.019066 + OuterRadius
NaraInnerLON2 = 4.741218 + OuterRadius

NaraOuterRingLAT = scipy.arange(NaraOuterLAT1, NaraOuterLAT2, 0.000001)
NaraOuterRingLAT = scipy.around(NaraOuterRingLAT, 6)

NaraOuterRingLON = scipy.arange(NaraOuterLON1, NaraOuterLON2, 0.000001)
NaraOuterRingLON = scipy.around(NaraOuterRingLON, 6)

if SolundirLAT in NaraOuterRingLAT and SolundirLON in NaraOuterRingLON:
    print('Solundir is in outer ring in Nara')

NaraInnerRingLAT = scipy.arange(NaraInnerLAT1, NaraInnerLAT2, 0.000001)
NaraInnerRingLAT = scipy.around(NaraInnerRingLAT, 6)

NaraInnerRingLON = scipy.arange(NaraInnerLON1, NaraInnerLON2, 0.000001)
NaraInnerRingLON = scipy.around(NaraInnerRingLON, 6)

if SolundirLAT in NaraInnerRingLAT and SolundirLON in NaraInnerRingLON:
    print('Solundir is in inner ring in Nara')