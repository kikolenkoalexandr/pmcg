from PyQt5 import QtWidgets
from pymodbus.client.sync import ModbusTcpClient
 
# Импортируем наш шаблон.
from mainWindow import Ui_MainWindow
import sys
 
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # подключение клик-сигнал к слоту btnClicked
        self.ui.SendButton.clicked.connect(self.btnSendClicked)
        self.ui.RequestButton.clicked.connect(self.btnRequestClicked)

    def btnSendClicked(self):
        client = ModbusTcpClient("127.0.0.1")
        hr_num = '1'
        client.write_register(int(hr_num),int(self.ui.HRvalueLineEdit.text()))#self.ui.HRvalueLineEdit.text
        client.close()

    def btnRequestClicked(self):
        client = ModbusTcpClient("127.0.0.1")
        hr_num = 1
        result = client.read_holding_registers(int(hr_num),1)
        self.ui.label.setText(str(result.registers[0]))
        client.close()

app = QtWidgets.QApplication([])
application = mywindow()
application.show()
 
sys.exit(app.exec())