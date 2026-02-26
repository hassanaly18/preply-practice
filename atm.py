class ATM:
    def __init__(self):
        self.__pin = None
        
    def setPin(self, newPin):
        if newPin >=1000 and newPin <=9999:
            self.__pin = newPin
        else:
            print("Invalid Pin")
    
    def getPin(self):
        print("Your atm pin:", self.__pin)                 