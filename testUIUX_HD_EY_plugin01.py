
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

#UI파일 연결. 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
vrTOC_form, vrTOC_base = uiTools.loadUiType("testUIUX_HD_EY_plugin01.ui")

#화면을 띄우는데 사용되는 Class 선언
class vrWindowClass(vrTOC_form, vrTOC_base):
    def __init__(self, parent=None) :
        #Setup and connect the plugins UI.
        super(vrWindowClass, self).__init__(parent)
        self.parent = parent
        self.setupUi(self)
        
        # 버튼 객체가 클릭되면 print 메서드 출력
        self.btn_1.clicked.connect(self.button1Function) 
        self.btn_2.clicked.connect(self.button2Function)

    def button1Function(self) :
        global comboBox_vset_list
        comboBox_vset_list = []
        
        print("btn_1 Clicked")
        vrVariants.selectVariantSet("func_creditCard") # func_creditCard vset을 선택해서 실행시킴
        vred_vset_list1 = vrVariantSets.getVariantSets() # 현재 오픈된 vred 파일에 있는 vset 들을 모두 가져와 list 형태로 리턴함
        print(vred_vset_list1)
        
        for element1 in vred_vset_list1 : # 가져온 vset lists 중에서
            if "func_" in element1:         # func_ 문자열을 가진 원소만 가져와
                comboBox_vset_list.append(element1)  # combobox에 들어갈 원소로 list up
                
        print(comboBox_vset_list)
        '''
        if "func_" in vred_vset_list1 : #comboBox에 들어갈 원소 func_만 찾아내서 새로운 list를 만듦
            comboBox_vset_list.append()
        print("comboBox_vset_list")
'''
    def button2Function(self) :
        print("btn_2 Clicked")

'''
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = vrWindowClass() 
    myWindow.show()
    app.exec_()
'''

if not importError:
    viewpointPlugin = vrWindowClass(VREDPluginWidget)
