# DemoForm.py
# Demoform.ui(화면단) + DemoForm.py(로직단)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#디자인 파일을 로딩
form_class = uic.loadUiType("DemoForm.ui")[0]

#윈도우 클래스 정의(처음에는 QDialog 상속)
class DemoForm(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self) #화면단 로딩
        self.label.setText("첫번째 PyQt데모")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoForm()
    demoWindow.show()
    sys.exit(app.exec_())
    