import Ratios
import math
class Gears:
    def __init__(self):
        self.R = Ratios.Ratios()
        self.tireD = (((self.R.tireW*(self.R.tireAR/100))*0.039370079)*2)+self.R.rimD

    def getAvg(self, r1, r2):
        return ((r1+r2)/2)

    def getGearingRatio(self, mph, rpm):
        return (math.pi * self.tireD * 60 * rpm) / (mph * 12 * 5280 * self.R.GF)

    def getGear(self, mph, rpm):
        gr = self.getGearingRatio(mph, rpm)
        gear = 0
        if(gr > self.getAvg(self.R.G1, self.R.G2)):
            gear = 1
        elif(gr < self.getAvg(self.R.G1, self.R.G2) and gr > self.getAvg(self.R.G2, self.R.G3)):
            gear = 2
        elif(gr < self.getAvg(self.R.G2, self.R.G3) and gr > self.getAvg(self.R.G3, self.R.G4)):
            gear = 3
        elif(gr < self.getAvg(self.R.G3, self.R.G4) and gr > self.getAvg(self.R.G4, self.R.G5)):
            gear = 4
        elif(gr < self.getAvg(self.R.G4, self.R.G5) and gr > self.getAvg(self.R.G5, self.R.G6)):
            gear = 5
        elif(gr < self.getAvg(self.R.G5, self.R.G6)):
            gear = 6
        else:
            gear = 0
        return gear
