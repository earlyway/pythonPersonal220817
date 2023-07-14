class TestAction(vrAEBase):
    global a
    global e
    a = vrDeviceService.getLeftTrackedHand()
    e = vrdTrackedHand.getPinchStrength(a)
    print("TestAction class")
    
    global leftController
    global numEight
    leftController = vrDeviceService.getVRDevice("left-controller")
    numEight = findNode("8")
    
    leftConstEight3 = None
    deleteC3 = False
    
    def __init__(self):
        vrAEBase.__init__(self)
        self.addLoop()
    
    def recEvent(self, state):
        vrAEBase.recEvent(self, state)
        
    def ConstOn(self):
        self.Clear()
        self.leftConstEight3 = vrConstraintService.createParentConstraint([leftController.getNode()], numEight, True)
        self.deleteC3 = True
        
    def ConstOff(self):
        self.Clear()
            
        print(str(vrConstraintService.getConstraints()))
        
        self.deleteC3 = False
        self.subLoop()
        
    def Clear(self):
        amount = vrConstraintService.getConstraints()
        for i in amount:
            vrConstraintService.deleteConstraint(i)
        
    def loop(self):
        e = vrdTrackedHand.getPinchStrength(a)
        print(str(e) + " getPinchStrength")
        if  self.deleteC3 == False and e > 0.6 :
            print(str(e) + " getPinchStrength ConsOn")
            self.ConstOn()
        elif self.deleteC3 == True and e <= 0.6 :
            print(str(e) + " getPinchStrength ConstOff")
            self.ConstOff()
            
cc = TestAction()