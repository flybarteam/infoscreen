import scipy
import getcoordinates
#Radius
OuterRadius = 0.0125
InnerRadius = 0.0015

#Simulated coordinates
SolundirLAT = round(getcoordinates.latitude, 6)
SolundirLON = round(getcoordinates.longitude, 6)

print(SolundirLAT)
print(SolundirLON)
###################################################
#Mjomna

MjomnaOuterLAT1 = 60.918404 - OuterRadius
MjomnaOuterLON1 = 4.901205 - OuterRadius
MjomnaOuterLAT2 = 60.918404 + OuterRadius
MjomnaOuterLON2 = 4.901205 + OuterRadius

MjomnaInnerLAT1 = 60.918404 - InnerRadius
MjomnaInnerLON1 = 4.901205 - InnerRadius
MjomnaInnerLAT2 = 60.918404 + InnerRadius
MjomnaInnerLON2 = 4.901205 + InnerRadius

MjomnaOuterRingLAT = scipy.arange(MjomnaOuterLAT1, MjomnaOuterLAT2, 0.000001)
MjomnaOuterRingLAT = scipy.around(MjomnaOuterRingLAT, 6)

MjomnaOuterRingLON = scipy.arange(MjomnaOuterLON1, MjomnaOuterLON2, 0.000001)
MjomnaOuterRingLON = scipy.around(MjomnaOuterRingLON, 6)

def isMjomnaOuterring():
    if SolundirLAT in MjomnaOuterRingLAT and SolundirLON in MjomnaOuterRingLON:
        print('Solundir is in outer ring in Mjomna')
        MjomnaOuterring = 1
    else:
        MjomnaOuterring = 0
    return MjomnaOuterring

MjomnaInnerRingLAT = scipy.arange(MjomnaInnerLAT1, MjomnaInnerLAT2, 0.000001)
MjomnaInnerRingLAT = scipy.around(MjomnaInnerRingLAT, 6)

MjomnaInnerRingLON = scipy.arange(MjomnaInnerLON1, MjomnaInnerLON2, 0.000001)
MjomnaInnerRingLON = scipy.around(MjomnaInnerRingLON, 6)

def isMjomnaInnerring():
        if SolundirLAT in MjomnaInnerRingLAT and SolundirLON in MjomnaInnerRingLON:
            print('Solundir is in inner ring in Mjomna')
            MjomnaInnerring = 1
        else:
            MjomnaInnerring = 0
        return MjomnaInnerring
#################################################################################
#Eivindvik

EivindvikOuterLAT1 = 60.979406 - OuterRadius
EivindvikOuterLON1 = 5.077910 - OuterRadius
EivindvikOuterLAT2 = 60.979406 + OuterRadius
EivindvikOuterLON2 = 5.077910 + OuterRadius

EivindvikInnerLAT1 = 60.979406 - InnerRadius
EivindvikInnerLON1 = 5.077910 - InnerRadius
EivindvikInnerLAT2 = 60.979406 + InnerRadius
EivindvikInnerLON2 = 5.077910 + InnerRadius

EivindvikOuterRingLAT = scipy.arange(EivindvikOuterLAT1, EivindvikOuterLAT2, 0.000001)
EivindvikOuterRingLAT = scipy.around(EivindvikOuterRingLAT, 6)

EivindvikOuterRingLON = scipy.arange(EivindvikOuterLON1, EivindvikOuterLON2, 0.000001)
EivindvikOuterRingLON = scipy.around(EivindvikOuterRingLON, 6)

def isEivindvikOuterring():
    if SolundirLAT in EivindvikOuterRingLAT and SolundirLON in EivindvikOuterRingLON:
        print('Solundir is in outer ring in Eivindvik')
        EivindvikOuterring = 1
    else:
        EivindvikOuterring = 0
    return EivindvikOuterring

EivindvikInnerRingLAT = scipy.arange(EivindvikInnerLAT1, EivindvikInnerLAT2, 0.000001)
EivindvikInnerRingLAT = scipy.around(EivindvikInnerRingLAT, 6)

EivindvikInnerRingLON = scipy.arange(EivindvikInnerLON1, EivindvikInnerLON2, 0.000001)
EivindvikInnerRingLON = scipy.around(EivindvikInnerRingLON, 6)

def isEivindvikInnerring():

    if SolundirLAT in EivindvikInnerRingLAT and SolundirLON in EivindvikInnerRingLON:
        print('Solundir is in inner ring in Eivindvik')
        EivindvikInnerring = 1
    else:
        EivindvikInnerring = 0
    return EivindvikInnerring
#####################################################################################
#Austrheim

AustrheimOuterLAT1 = 60.789151 - OuterRadius
AustrheimOuterLON1 = 4.939859 - OuterRadius
AustrheimOuterLAT2 = 60.789151 + OuterRadius
AustrheimOuterLON2 = 4.939859 + OuterRadius

AustrheimInnerLAT1 = 60.789151 - InnerRadius
AustrheimInnerLON1 = 4.939859 - InnerRadius
AustrheimInnerLAT2 = 60.789151 + InnerRadius
AustrheimInnerLON2 = 4.939859 + InnerRadius

AustrheimOuterRingLAT = scipy.arange(AustrheimOuterLAT1, AustrheimOuterLAT2, 0.000001)
AustrheimOuterRingLAT = scipy.around(AustrheimOuterRingLAT, 6)

AustrheimOuterRingLON = scipy.arange(AustrheimOuterLON1, AustrheimOuterLON2, 0.000001)
AustrheimOuterRingLON = scipy.around(AustrheimOuterRingLON, 6)

def isAustrheimOuterring():

    if SolundirLAT in AustrheimOuterRingLAT and SolundirLON in AustrheimOuterRingLON:
        print('Solundir is in outer ring in Austrheim')
        AustrheimOuterring = 1
    else:
        AustrheimOuterring = 0
    return AustrheimOuterring

AustrheimInnerRingLAT = scipy.arange(AustrheimInnerLAT1, AustrheimInnerLAT2, 0.000001)
AustrheimInnerRingLAT = scipy.around(AustrheimInnerRingLAT, 6)

AustrheimInnerRingLON = scipy.arange(AustrheimInnerLON1, AustrheimInnerLON2, 0.000001)
AustrheimInnerRingLON = scipy.around(AustrheimInnerRingLON, 6)

def isAustrheimInnerring():

    if SolundirLAT in AustrheimInnerRingLAT and SolundirLON in AustrheimInnerRingLON:
        print('Solundir is in inner ring in Austrheim')
        AustrheimInnerring = 1
    else:
        AustrheimInnerring = 0
    return AustrheimInnerring

###########################################################################
#Nara

NaraOuterLAT1 = 61.019066 - OuterRadius
NaraOuterLON1 = 4.741218 - OuterRadius
NaraOuterLAT2 = 61.019066 + OuterRadius
NaraOuterLON2 = 4.741218 + OuterRadius

NaraInnerLAT1 = 61.019066 - InnerRadius
NaraInnerLON1 = 4.741218 - InnerRadius
NaraInnerLAT2 = 61.019066 + InnerRadius
NaraInnerLON2 = 4.741218 + InnerRadius

NaraOuterRingLAT = scipy.arange(NaraOuterLAT1, NaraOuterLAT2, 0.000001)
NaraOuterRingLAT = scipy.around(NaraOuterRingLAT, 6)

NaraOuterRingLON = scipy.arange(NaraOuterLON1, NaraOuterLON2, 0.000001)
NaraOuterRingLON = scipy.around(NaraOuterRingLON, 6)

def isNaraOuterring():
    if SolundirLAT in NaraOuterRingLAT and SolundirLON in NaraOuterRingLON:
        print('Solundir is in outer ring in Nara')
        NaraOuterring = 1
    else:
        NaraOuterring = 0
    return NaraOuterring

NaraInnerRingLAT = scipy.arange(NaraInnerLAT1, NaraInnerLAT2, 0.000001)
NaraInnerRingLAT = scipy.around(NaraInnerRingLAT, 6)

NaraInnerRingLON = scipy.arange(NaraInnerLON1, NaraInnerLON2, 0.000001)
NaraInnerRingLON = scipy.around(NaraInnerRingLON, 6)

def isNaraInnerring():
    if SolundirLAT in NaraInnerRingLAT and SolundirLON in NaraInnerRingLON:
        print('Solundir is in inner ring in Nara')
        NaraInnerring = 1
    else:
        NaraInnerring = 0
    return NaraInnerring

########################################################################
#Bergen
#Bergen

BergenOuterLAT1 = 60.369379 - OuterRadius
BergenOuterLON1 = 5.352979 - OuterRadius
BergenOuterLAT2 = 60.369379 + OuterRadius
BergenOuterLON2 = 5.352979 + OuterRadius

BergenInnerLAT1 = 60.369379 - InnerRadius
BergenInnerLON1 = 5.352979 - InnerRadius
BergenInnerLAT2 = 60.369379 + InnerRadius
BergenInnerLON2 = 5.352979 + InnerRadius

BergenOuterRingLAT = scipy.arange(BergenOuterLAT1, BergenOuterLAT2, 0.000001)
BergenOuterRingLAT = scipy.around(BergenOuterRingLAT, 6)

BergenOuterRingLON = scipy.arange(BergenOuterLON1, BergenOuterLON2, 0.000001)
BergenOuterRingLON = scipy.around(BergenOuterRingLON, 6)

def isBergenOuterring():
    if SolundirLAT in BergenOuterRingLAT and SolundirLON in BergenOuterRingLON:
        BergenOuterring = 1
    else:
        BergenOuterring = 0
    return BergenOuterring

BergenInnerRingLAT = scipy.arange(BergenInnerLAT1, BergenInnerLAT2, 0.000001)
BergenInnerRingLAT = scipy.around(BergenInnerRingLAT, 6)

BergenInnerRingLON = scipy.arange(BergenInnerLON1, BergenInnerLON2, 0.000001)
BergenInnerRingLON = scipy.around(BergenInnerRingLON, 6)

def isBergenInnerring():
        if SolundirLAT in BergenInnerRingLAT and SolundirLON in BergenInnerRingLON:
            BergenInnerring = 1
        else:
            BergenInnerring = 0
        return BergenInnerring
