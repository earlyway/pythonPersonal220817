
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Signal,Slot, QThread,QTimer

importError = False
try:
    import vrController
    import vrFileIO
    import vrMovieExport
    import vrOSGWidget
    import vrScenegraph
    import vrNodePtr
    import vrVariantSets
    import vrVariants
    import time
except ImportError:
    importError = True
    pass

import uiTools

listToLoad = False
global comboBox_vset_list
comboBox_vset_list = []


vrTOC_form, vrTOC_base = uiTools.loadUiType("010.ui")


class vrWindowClass(vrTOC_form, vrTOC_base):
    def __init__(self, parent=None) :
        #Setup and connect the plugins UI.
        super(vrWindowClass, self).__init__(parent)
        parent.layout().addWidget(self)
        self.parent = parent
        self.setupUi(self)
        
        self.ui_pushbutton_load.clicked.connect(self.loadFunction) 
        self.ui_pushbutton_reset.clicked.connect(self.resetFunction)
        
        
        
        self.syncComboBox()
        
        self.vset_select_combo_box1.clicked.connect(self.cbBox1)
        self.vset_select_combo_box2.clicked.connect(self.cbBox2)
        '''
        self.vset_select_combo_box1_radio_on.clicked.connect(self.radioBox1)
        self.vset_select_combo_box1_radio_off.clicked.connect(self.radioBox1)
        
        self.vset_select_combo_box2_radio_on.clicked.connect(self.radioBox2)
        self.vset_select_combo_box2_radio_off.clicked.connect(self.radioBox2)
'''

    def loadFunction(self) :
        self.vset_select_combo_box1.clear() #초기화
        self.vset_select_combo_box2.clear() #초기화
        comboBox_vset_list = [] #load 버튼을 누를때마다 combobox list를 초기화. 이걸 하지않으면 list가 쌓임.
        
        vrVariants.selectVariantSet("func_creditCard")
        vred_vset_list1 = vrVariantSets.getVariantSets()
        print(vred_vset_list1)
        
        for element1 in vred_vset_list1 : 
            if "func_" in element1:         
                comboBox_vset_list.append(element1)  
                
        print("comboBox vset list = " + str(comboBox_vset_list))
        
        self.vset_select_combo_box1.addItems(comboBox_vset_list)
        self.vset_select_combo_box2.addItems(comboBox_vset_list)
        
    def resetFunction(self) :
        print("reset btn Clicked")
        
    def syncComboBox(self) :
        for i in range(0, self.comboBox_vset_list.count()):
            print("sync "+ i)
            '''
    def radioBox1(self):
        if self.vset_select_combo_box1_radio_on.isChecked() : print("box1 on checked")
        elif self.vset_select_combo_box1_radio_off.isChecked() : print("box1 off checked")
        
    def radioBox2(self):
        if self.vset_select_combo_box2_radio_on.isChecked() : print("box2 on checked")
        elif self.vset_select_combo_box2_radio_off.isChecked() : print("box2 off checked")
'''

if not importError:
    viewpointPlugin = vrWindowClass(VREDPluginWidget)
