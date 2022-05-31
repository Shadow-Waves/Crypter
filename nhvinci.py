from sympy import Function,symbols,sqrt,log
from PyQt6.QtWidgets import QApplication,QMainWindow,QLineEdit,QComboBox,QTextEdit,QPushButton
from PyQt6.QtGui import QIcon
from sys import argv
from re import match

class NHVinci(QMainWindow):
    def __init__(self,):
        super().__init__()

        self.symbol_x = symbols("x")
        self.f,self.g = Function("f")(self.symbol_x),Function("g")(self.symbol_x)
        self.f,self.g = 9*log(self.symbol_x,10)*((1.0 + sqrt(5.0))/(2.0)),((10)**((2.0)*self.symbol_x/(1 + sqrt(5))))**(1.0/9)

        self.setWindowTitle("NHVinci")
        self.setWindowIcon(QIcon("phi.png"))
        self.setFixedSize(600,600)
        self.setStyleSheet("background-color:black;")

        self.input = QLineEdit(self)
        self.input.setGeometry(50,50,300,50)
        self.input.setStyleSheet("background-color:transparent;color:cyan;border:1px groove lightgreen;border-radius:10px;font-size:16px;font-weight:bold;")
        self.input.setPlaceholderText("INPUT")

        self.method = QComboBox(self)
        self.method.setGeometry(400,50,150,50)
        self.method.setStyleSheet('background-color:transparent;color:magenta;border:0px groove lightgreen;border-radius:5px;font-size:20px;font-weight:bold;')
        self.method.addItem(QIcon("1.png"),"Crypting","Encrypting")
        self.method.addItem(QIcon("2.png"),"Decrypting","Decrypting")
        self.method.currentIndexChanged.connect(self.method_changed)

        self.ok = QPushButton("Do",self)
        self.ok.setGeometry(270,110,30,30)
        self.ok.setStyleSheet("color:white;border:1px groove blue;border-radius:5px;font-size:20px;font-weight:bold;")
        self.ok.clicked.connect(self.eventing)

        self.output = QTextEdit(self)
        self.output.setGeometry(50,150,500,400)
        self.output.setPlaceholderText("OUTPUT")
        self.output.setStyleSheet("background-color:rgba(150,200,170,0.3);color:yellow;font-size:20px;")
        self.output.setReadOnly(True)
        self.output.verticalScrollBar().setStyleSheet("QScrollBar:vertical {"              
            "    border: 0px solid transparent;"
            "    background:white;"
            "    width:5px;    "
            "    margin: 0px 0px 0px 0px;"
            "}"
            "QScrollBar::handle:vertical {"
            "    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,"
            "    stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130), stop:1 rgb(32, 47, 130));"
            "    min-height: 0px;"
            "}"
            "QScrollBar::add-line:vertical {"
            "    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,"
            "    stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));"
            "    height: 0px;"
            "    subcontrol-position: bottom;"
            "    subcontrol-origin: margin;"
            "}"
            "QScrollBar::sub-line:vertical {"
            "    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,"
            "    stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));"
            "    height: 0 px;"
            "    subcontrol-position: top;"
            "    subcontrol-origin: margin;"
        "}")

        self.show()
    
    def eventing(self):
        if not self.method.currentIndex():
            if self.input.text():
                self.output.setText(self.code(self.input.text()))
                self.input.setText("")
        else:
            if self.input.text() and match(r"[\d\.\$\|]+",self.input.text()):
                self.output.setText(self.decode(self.input.text()))
                self.input.setText("")
            else:
                self.output.setText("Empty Input Or Invalid Code Please Check Your Code... The Code Is Constructed Of The Following Characters < digits(0,1,2,3,4,5,6,7,8,9) , dot(.) , dual-or(||) and dollar-sign($) >")

    def method_changed(self):
        self.input.setText("")
        self.output.setText("")


    def code(self,string):
        return "".join([str(self.f.subs(self.symbol_x,ord(item)).evalf()) + "$" if item != " " else "||" for item in string.upper()]).rstrip("$")

    def decode(self,expr):
        return "".join([chr(round(self.g.subs(self.symbol_x,float(element)).simplify().evalf())) if element else " " for item in expr.split("||") for element in item.split("$")])

if __name__ == "__main__":
    application = QApplication(argv)
    nhvinci = NHVinci()
    application.exec()