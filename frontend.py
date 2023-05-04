from tkinter import *
from backend import SmartHome, SmartOven, SmartPlug

mainWin = Tk()
mySmartHome = SmartHome()

deviceToggleButtons = []
deviceDeleteButtons = []
deviceModifyButtons = []
addDeviceButtons = []
deviceLabels = []
devicesOnLabels = []

def setupSmartHome():
    
    """
    The setupSmartHome function is used to test the adding functionality of smart devices to mySmartHome required in task 4
    
    Returns: 
    Values of setupSmartHome in the terminal - list of devices and their attributes.
    """
    
    smartPlug1 = SmartPlug("Smart Plug 1", "Smart Plug", 0, 150, 0)
    smartOven1 = SmartOven("Smart Oven 1", "Smart Oven", 0, 260, 0)
    smartPlug2 = SmartPlug("Smart Plug 2", "Smart Plug", 0, 150, 0)
    smartPlug3 = SmartPlug("Smart Plug 3", "Smart Plug", 0, 150, 0)
    smartOven2 = SmartOven("Smart Oven 2", "Smart Oven", 0, 260, 0)

    mySmartHome.addDevice(smartPlug1)
    mySmartHome.addDevice(smartOven1)
    mySmartHome.addDevice(smartPlug2)
    mySmartHome.addDevice(smartPlug3)
    mySmartHome.addDevice(smartOven2)
    
    smartOven1.toggleDevice()
     
def setupMainWin():
    
    """
    The setupMainWin function is used to initialise the Main GUI for the rest of the tasks required in task 5
    
    Returns: 
    Opens the main window which displays the list of devices and their attributes along with buttons that can be used to interact with each device.
    """
    
    numberOfDevices = mySmartHome.getNumberOfDevices()
    
    mainWin.title("Smart Home Devices")
    mainWin.geometry("900x400")
    mainWin.resizable(width=True, height=True)
    
    titleLabel = Label(mainWin, text="Smart Home")
    titleLabel.grid(row=0, column=1, padx=25, pady=10, sticky="w")
    titleLabel.config(font=("TkDefaultFont", 12, "bold"))
    
    def turnOnAll():
    
        """
        The turnOnAll function is used to turn on all devices in mySmartHome
        """
        
        mySmartHome.turnOnAll()
        listDevices()
    
    turnOnAllBtn = Button(mainWin, text="Turn On All Devices", command=turnOnAll)
    turnOnAllBtn.grid(row=1, column=1, padx=25, pady=5, sticky="w")
    
    def turnOffAll():
    
        """
        The turnOffAll function is used to turn off all devices in mySmartHome
        """
    
        mySmartHome.turnOffAll()
        listDevices()
        
    turnOffAllBtn = Button(mainWin, text="Turn Off All Devices", command=turnOffAll)
    turnOffAllBtn.grid(row=1, column=1, padx=140, pady=5)  

    quitBtn = Button(mainWin, text="Quit", command=mainWin.destroy)
    quitBtn.grid(row=1, column=4, padx=0, pady=5, sticky="e")
    setupSmartHome()
    
    listDevices()
    listButtons()
    
    mainWin.mainloop()

def listButtons():
    
    """
    The listButtons function is used to initialise the buttons attached to each device on the MainWin required in task 4
    
    Returns: 
    A list of devices in the smart home.
    """
    
    numberOfDevices = len(mySmartHome.devices)
    
    for button in range(len(deviceToggleButtons)):
        deviceToggleButtons[0].destroy()
        del deviceToggleButtons[0]
    for button in range(len(deviceModifyButtons)):
        deviceModifyButtons[0].destroy()
        del deviceModifyButtons[0]
    for button in range(len(deviceDeleteButtons)):
        deviceDeleteButtons[0].destroy()
        del deviceDeleteButtons[0]
        
    for deviceIndex in range(len(deviceLabels)):
        
        def toggleDeviceLink(i = deviceIndex):
            toggleDevice(i)
                        
        toggleButton = Button(mainWin, text="Toggle Device", command=toggleDeviceLink)
        toggleButton.grid(row=(deviceIndex + 2), column=2, padx=0, pady=5)
        
        def modifyDeviceLink(i = deviceIndex):
            modifyDevice(i)
            
        modifyDeviceBtn = Button(mainWin, text="Modify", command=modifyDeviceLink)
        modifyDeviceBtn.grid(row=(deviceIndex + 2), column=3, padx=10, pady=5, sticky="w")
        
        def deleteDeviceLink(i = deviceIndex):
            deleteDevice(i)
        
        deleteDeviceBtn = Button(mainWin, text="Delete", command=deleteDeviceLink)
        deleteDeviceBtn.grid(row=(deviceIndex + 2), column=4, padx=0, pady=5, sticky="e")
        
        deviceToggleButtons.append(toggleButton)
        deviceModifyButtons.append(modifyDeviceBtn)
        deviceDeleteButtons.append(deleteDeviceBtn)
            
    numberOfDevices += 1
    
    if len(deviceLabels) == 0:
        
        numberOfDevices = 1
                
    addDeviceBtn = Button(mainWin, text="Add More Devices", command=addDevice) 
    addDeviceBtn.grid(row=numberOfDevices + 3, column=1, padx=25, pady=5, sticky="w")
    
    addDeviceButtons.append(addDeviceBtn)
    
def deleteDevice(deviceIndex):
    
    """
    The deleteDevice function is used to delete a device from the list of devices on the MainWin.
    """
    
    del mySmartHome.devices[deviceIndex]
    
    for k in range(len(addDeviceButtons)):
        
        addDeviceButtons[0].destroy()
        addDeviceButtons.pop(0)
        
    for j in range(len(devicesOnLabels)):
        
        devicesOnLabels[0].destroy()
        devicesOnLabels.pop(0)
    
    listDevices()
    listButtons()
    
def addDevice():
    
    """
    The addDevice function is used to add a device to the list of devices on the MainWin.
    """
    
    addDeviceWin = Toplevel()
    addDeviceWin.geometry("400x150")
    addDeviceWin.resizable(width=True, height=True)
    addDeviceWin.title("Add a Device")
        
    titleLabel = Label(addDeviceWin, text="Add a Device to your Smart Home")
    titleLabel.grid(row=0, column=1, padx=25, pady=10, sticky="w")
    titleLabel.config(font=("TkDefaultFont", 12, "bold"))
    
    def addSmartPlug():
        
        """
        The addSmartPlug function is used to add a Smart Plug to the list of devices on the MainWin.
        """
        
        customSmartPlug = SmartPlug("Custom Smart Plug", "Smart Plug", 0, 150, 0)
        mySmartHome.addDevice(customSmartPlug)

        for i in range(len(devicesOnLabels)):
            devicesOnLabels[0].destroy()
            devicesOnLabels.pop(0)

        for i in range(len(devicesOnLabels)):
            devicesOnLabels[0].destroy()
            devicesOnLabels.pop(0)
            
        for i in range(len(addDeviceButtons)):
            addDeviceButtons[0].destroy()
            addDeviceButtons.pop(0)  
        
        listDevices()
        listButtons()
    
    addSmartPlugBtn = Button(addDeviceWin, text="Add Smart Plug", command=addSmartPlug)
    addSmartPlugBtn.grid(row=1, column=1, padx=25, pady=10, sticky="w")
    
    def addSmartOven():
        
        """
        The addSmartOven function is used to add a Smart Oven to the list of devices on the Main
        """
        
        customSmartOven = SmartOven("Custom Smart Oven", "Smart Oven", 0, 260, 0)
        mySmartHome.addDevice(customSmartOven)
        
        for i in range(len(devicesOnLabels)):
            devicesOnLabels[0].destroy()
            devicesOnLabels.pop(0)
            
        for i in range(len(addDeviceButtons)):
            addDeviceButtons[0].destroy()
            addDeviceButtons.pop(0)
            
        listDevices()
        listButtons()
            
    addSmartOvenBtn = Button(addDeviceWin, text="Add Smart Oven", command=addSmartOven)
    addSmartOvenBtn.grid(row=2, column=1, padx=25, pady=10, sticky="w")
    
    deviceIndex = len(mySmartHome.devices) - 1
    
    cancelBtn = Button(addDeviceWin, text="Cancel", command=addDeviceWin.destroy)
    cancelBtn.grid(row=0, column=2, padx=10, pady=10)
    
def listDevices():
    
    """
    The listDevices function is used to initialise the list of devices on the MainWin required in task 4
    """

    numberOfDevices = mySmartHome.getNumberOfDevices()
    
    for label in range(len(deviceLabels)):
        deviceLabels[0].destroy()
        del deviceLabels[0]
    
    if numberOfDevices == 0:
        height = 50
    elif numberOfDevices == 1:
        height = 175
    else:
        height = (40 * (numberOfDevices + 2)) + 50
        
    devicesOnValue = 0
    
    for deviceIndex in range(numberOfDevices):

        device = mySmartHome.getDeviceAt(deviceIndex)
        
        currentWin = "{}x{}".format(len(str(device)) + 560, height)
        if currentWin > mainWin.geometry("{}x{}".format(len(str(device)) + 550, height)):
            mainWin.geometry("{}x{}".format(len(str(device)) + 560, height + 35))
            
        deviceTxt = Label(mainWin, text="{}".format(device))
        deviceTxt.grid(row=(deviceIndex + 2), column=1, padx=25, pady=10, sticky="w")
        
        if mySmartHome.getState(deviceIndex):
            devicesOnValue = devicesOnValue + 1
            
        deviceLabels.append(deviceTxt)
        
    if len(deviceLabels) == 0:

        noDeviceLbl = Label(mainWin, text="There are no devices in this Smart Home")
        deviceLabels.append(noDeviceLbl)
        noDeviceLbl.grid(row=2, column=1, padx=25, pady=10, sticky="w")
        numberOfDevices = 1
               
    devicesOnLbl = Label(mainWin, text="Number of devices Turned On: {}".format(str(devicesOnValue)))
    devicesOnLbl.grid(row=numberOfDevices + 2, column=1, padx=25, pady=5, sticky="w")
    
    devicesOnLabels.append(devicesOnLbl)

def modifyDevice(deviceIndex):
    
    """
    The modifyDevice function is used to modify a device on the list of devices on the MainWin.
    """

    modifyWin = Toplevel()
    modifyWin.geometry("500x220")
    modifyWin.resizable(width=True, height=True)
    device = mySmartHome.getDeviceAt(deviceIndex)
    modifyWin.title("Modify Device - {}".format(device.name))
    
    titleLabel = Label(modifyWin, text="Configure Smart Home Device - {}".format(device.name))
    titleLabel.grid(row=0, column=1, padx=10, pady=0, sticky="w")
    titleLabel.config(font=("TkDefaultFont", 12, "bold"))
    
    if device.deviceType == "Smart Plug":
        attributeName = "Consumption Rate: "
        attributeValue = device.getConsumptionRate()
        maximumSliderValue = device.maximumConsumptionRate
        minimumSliderValue = device.minimumConsumptionRate
    elif device.deviceType == "Smart Oven":
        attributeName = "Temperature: "
        attributeValue = device.getTemperature()
        maximumSliderValue = device.maximumTemperature
        minimumSliderValue = device.minimumTemperature
    
    currentNameLabel = Label(modifyWin, text="Current Device Name: {}".format(device.name))
    currentNameLabel.grid(row=1, column=1, padx=10, pady=10, sticky="w")
    
    newDeviceNameTxt = Entry(modifyWin)
    newDeviceNameTxt.insert(0, device.name)
    newDeviceNameTxt.grid(row=2, column=1, padx=20, pady=0, sticky="w")
    newDeviceNameTxt.config(font=("TkDefaultFont", 12))
    newDeviceName = newDeviceNameTxt.get()
    
    currentValueLabel = Label(modifyWin, text="Current Device {}: {}".format(attributeName, attributeValue))
    currentValueLabel.grid(row=3, column=1, padx=10, pady=10, sticky="w")
    
    newAttributeSlider = Scale(modifyWin, from_=minimumSliderValue, to=maximumSliderValue, orient=HORIZONTAL)
    newAttributeSlider.grid(row=4, column=1, padx=20, pady=0, sticky="nw")
    newAttributeValue = newAttributeSlider.get()
    
    def updateLink(i = newDeviceName, j = newAttributeValue):
        updateSmartDevice(i, j)
    
    def updateSmartDevice(newDeviceName, newAttributeValue):
        newDeviceName = newDeviceNameTxt.get()
        newAttributeValue = newAttributeSlider.get()
        device.name = newDeviceName
        if device.deviceType == "Smart Plug":
            device.setConsumptionRate(newAttributeValue)
        elif device.deviceType == "Smart Oven":
            device.setTemperature(newAttributeValue)
        listDevices()
        updateDeviceIndexes()
        modifyWin.destroy()
    
    updateButton = Button(modifyWin, text="Ok", command=lambda: updateLink())
    updateButton.grid(row=1, column=3)
    
    cancelBtn = Button(modifyWin, text="Cancel", command=modifyWin.destroy)
    cancelBtn.grid(row=0, column=3, padx=10, pady=10)

def updateDeviceIndexes():
    
    """
    Used to update the indexes of the devices in the list of devices on the MainWin, a workaround for when a device has been changed, updates the indexes of each device.
    """
    
    for i, device in enumerate(mySmartHome.devices):
        device.index = i
    
def toggleDevice(deviceIndex):
    
    """
    The toggleDevice function is used to switch the state of a device on the list of devices on the MainWin.
    """
    
    mySmartHome.toggleDevice(deviceIndex)
    
    listDevices()
    updateDeviceIndexes()

def main():
    
    """
    The main function is used as a shell to execute the program and begin it running through the steps.
    """    
    
    setupMainWin()
    
main()