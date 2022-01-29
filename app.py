# Importing everything in the app_ui script:
from app_ui import *
import random
import pyperclip as pc

upper_case = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lower_case = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','u','w','x','y','z']
symbol = ['#','-','=','*','/']
numbers = ['1','2','3','4','5','6','7','8','9','0']

# New class that will represent our main window (MainWindow), 
# Inherit from the QMainWindow Widget of PyQt 
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    password = []
    str_password = ""
    
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        # setupUi method responsible for generating the interface
        self.setupUi(self)
        
        self.horizontalSlider.setRange(4, 40)
        self.horizontalSlider.setPageStep(1)
        self.horizontalSlider.setValue(10)
        self.horizontalSlider.valueChanged.connect(self.updateLabel)
        
        self.pushButton.clicked.connect(self.button_password)

        self.pushButton_2.clicked.connect(self.copy_password)
                
    def updateLabel(self, value):
        self.label_6.setText(str(value))
          
    def button_password(self):
        characters = []
        size = self.horizontalSlider.value()
        upper_state = self.checkBox.isChecked()
        lower_state = self.checkBox_2.isChecked()
        numbers_state = self.checkBox_3.isChecked()
        symbols_state = self.checkBox_4.isChecked()
        
        if upper_state == True:
            characters = characters + upper_case
        if lower_state == True:
            characters = characters + lower_case
        if numbers_state == True:
            characters = characters + numbers
        if symbols_state == True:
            characters = characters + symbol

        self.password = []
        for i in range(size):
            random_characters = random.choice(characters)
            self.password.append(random_characters)
        
        self.set_password(self.password)
    
    def set_password(self, list_password):
        self.str_password = ''.join(list_password)
        self.label_4.setText(self.str_password)
        self.update()
        
    def copy_password(self):
        pc.copy(self.str_password)

# Init the app
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()