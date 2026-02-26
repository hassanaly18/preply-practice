class Phone:
    def __init__(self, model, battery):
        self.model = model        #public
        self.__battery = battery  #private
        
    def show(self):
        print("Battery: ", self.__battery)  
     
    def change(self):
        self.__battery = self.__battery-5   
        print("New Battery: ", self.__battery)  
    
    def newBattery(self, new):
        self.__battery = new 
        print("New Battery: ", self.__battery)      
           