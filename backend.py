class SmartHome:
    
    """
    A class representing a smart home.

    Attributes:
    devices: A list of all the devices in the smart home.
    state: The state of the smart home, i.e., whether it's on or off.
    """

    def __init__(self):
        
        """
        Initializes a new instance of the SmartHome class.
        """
        
        self.devices = []
        self.state = False

    def getDevices(self):
        
        """
        Returns a list of all the devices in the smart home.
        """
        
        return self.devices

    def getDeviceAt(self, index):
        
        """
        Returns the device at the specified index.

        Args:
        index(int): The index of the device to be retrieved.
        """
        
        return self.devices[index]

    def getNumberOfDevices(self):
        
        """
        Returns the number of devices in the smart home.
        """
        
        return len(self.devices)
    
    def getState(self, index):
        
        """
        Returns the state of the device at the specified index.

        Args:
        index(int): The index of the device whose state is to be retrieved.
        """
        
        return self.devices[index].state
        
    def addDevice(self, device):
        
        """
        Adds a new device to the smart home.
        """
        
        self.devices.append(device)
                
    def toggleDevice(self, index):
        
        """
        Toggles the state of the device at the specified index.
        
        index: The index of the device to be toggled.
        """
        
        self.devices[index].toggleDevice()
        
    def turnOnAll(self):
        
        """
        Turns on all the devices in the smart home.
        """
        
        numberOfDevices = len(self.devices)
            
        for device in range(numberOfDevices):
                        
            if not self.getState(device):
                                        
                self.toggleDevice(device)                    
                                            
    def turnOffAll(self):
        
        """
        Turns off all the devices in the smart home.
        """
        
        numberOfDevices = len(self.devices)
                
        for device in range(numberOfDevices):
                        
            if self.getState(device):
                    
                self.toggleDevice(device)
                
    def updateDevice(self, deviceName, value):
        
        """
        Updates the specified device with the new value.

        deviceName: The name of the device to be updated.
        value: The new value to be assigned to the device.
        """
        
        for device in self.devices:
            if device.name == deviceName:
                if device.deviceType == "Smart Plug":
                    if value > 150:
                        print("Error: consumptionRate cannot exceed 150.")
                        return
                    elif value < 0:
                        print("Error: consumptionRate cannot be negative.")
                        return
                    device.consumptionRate = value
                    return
                elif device.deviceType == "Smart Oven":
                    device.setTemperature(value)
                    return
        print("Error: device not found.")

    def __str__(self):
        
        """
        Returns a string representation of the smart home.
        """
        
        deviceList = []
        
        for device in self.devices:
            
            deviceList.append(str(device))
        
        return "Smart Home devices: \n" + "\n".join(deviceList)

class SmartDevice:
    
    """
    The SmartDevice class is used to declare the universal attributes of each device, such as the name, state, and device type
    """

    def __init__(self, name, deviceType):
        
        """
        Initializes a new instance of the SmartDevice class.
        """
        
        self.name = name
        self.state = False
        self.deviceType = deviceType

    def toggleDevice(self):
        
        """
        Toggles the state of the device between on and off.
        """
        
        self.state = not self.state

    def getState(self):
        
        """
        Returns the current state of the device.
        """
        
        return self.state

class SmartPlug(SmartDevice):
    
    """
    The SmartPlug class represents a smart plug device.
    """

    def __init__(self, name, deviceType, consumptionRate, maximumConsumptionRate, minimumConsumptionRate):
        
        """
        Initializes a new instance of the SmartPlug class.
        """
        
        super().__init__(name, deviceType)
        self.consumptionRate = consumptionRate
        self.maximumConsumptionRate = maximumConsumptionRate
        self.minimumConsumptionRate = minimumConsumptionRate

    def setConsumptionRate(self, rate):
        
        """
        Sets the current consumption rate of the device.
        """
        
        self.consumptionRate += rate

    def getConsumptionRate(self):
        
        """
        Returns the current consumption rate of the device.
        """
        
        return self.consumptionRate

    def __str__(self):
        
        """
        Returns a string representation of the device.
        """
        
        status = "on" if self.getState() else "off"
        return f"{self.name} is {status} - Consumption Rate: {self.consumptionRate}"
        
class SmartOven(SmartDevice):
    
    """
    The SmartOven class is a subclass of SmartDevice, representing a smart oven device. 
    It allows the user to set and get the temperature of the oven.
    """

    def __init__(self, name, deviceType, temperature, maximumTemperature, minimumTemperature):
        
        """
        Initializes a new instance of the SmartOven class.
        """
        
        super().__init__(name, deviceType)
        self.temperature = temperature
        self.temperature = 0
        self.maximumTemperature = maximumTemperature
        self.minimumTemperature = minimumTemperature

    def setTemperature(self, temperature):
        
        """
        Sets the temperature of the oven to the given value.
        """
        
        self.temperature = temperature

    def getTemperature(self):
        
        """
        Gets the current temperature of the oven.
        """
        
        return self.temperature

    def __str__(self):
        
        """
        Returns a string representation of the SmartOven instance.
        """
        
        status = "on" if self.getState() else "off"
        return f"{self.name} is {status} - Temperature: {self.temperature} Degrees Celsius"
    
def testSmartPlug():
    
    """
    The testSmartPlug function is used to test the smart plug functionality required in task 1
    """
    
    myPlug = SmartPlug("Smart Plug 1", "Smart Plug", 0, 150, 0)
    myPlug.toggleDevice()
    print("Smart Plug State:", myPlug.getState())
    print("Smart Plug Consumption Rate:", myPlug.getConsumptionRate())
    myPlug.setConsumptionRate(10)
    print("Smart Plug Consumption Rate:", myPlug.getConsumptionRate())
    print(myPlug) 
    
def testSmartOven():
    
    """
    The testSmartOven function is used to test the smart oven functionality required in task 2
    
    Returns: 
    Values of myOven
    """
    
    myOven = SmartOven("Smart Oven 1", "Smart Oven", 0, 260, 0)
    myOven.toggleDevice()
    print("Smart Oven State:", myOven.getState())
    print("Smart Oven Temperature:", myOven.getTemperature())
    myOven.setTemperature(180)
    print("Smart Oven Temperature:", myOven.getTemperature())
    print(myOven)
    
def testSmartHome():

    """
    The testSmartHome function is used to test the smart Home functionality required in task 3
    
    Returns: 
    Values of mySmartHome in the terminal
    """

    myHome = SmartHome()
    plug1 = SmartPlug("Smart Plug 1", "Smart Plug", 0, 150, 0)
    plug2 = SmartPlug("Smart Plug 2", "Smart Plug", 0, 150, 0)
    oven = SmartOven("Smart Oven 1", "Smart Oven", 0, 260, 0)
    plug2.toggleDevice()
    plug2.setConsumptionRate(45)
    oven.setTemperature(180)
    myHome.addDevice(plug1)
    myHome.addDevice(plug2)
    myHome.addDevice(oven)
    print(myHome)
    myHome.turnOnAll()
    print(myHome)
    
def main():
    
    """
    A function to test the smart Home functionality in task 1, 2 and 3
    """
    
    pass
    #testSmartPlug()
    #testSmartOven()
    #testSmartHome()
    
main()
 