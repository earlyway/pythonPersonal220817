
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
        print("btn_1 Clicked")
        vrVariants.selectVariantSet("func_creditCard")

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
