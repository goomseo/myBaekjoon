def isTroyMartian(antennas, eyes):
    return antennas >= 3 and eyes <= 4

def isVladSaturnian(antennas, eyes):
    return antennas <= 6 and eyes >= 2

def isGraemeMercurian(antennas, eyes):
    return antennas <= 2 and eyes <= 3

def main():
    antennas, eyes = [int(input()) for _ in range(2)]
    
    if isTroyMartian(antennas, eyes):
        print('TroyMartian')
    if isVladSaturnian(antennas, eyes):
        print('VladSaturnian')
    if isGraemeMercurian(antennas, eyes):
        print('GraemeMercurian')
        
main()