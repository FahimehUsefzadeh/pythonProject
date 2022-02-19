def main_menu():
    while True:
        print('1.Add contact')
        print('2.list')
        print('3.search by name')
        print('4.search by mobile')
        print('0.Exit')
    choice = input('enter a choice:')
    if choice == '1':
        add_contact()







import sys
from PyQt5.QtWidgets import QDialog
from PyQt5.Qtwidgets import QApplication
from PyQt5.Qtwidgets import QLabel
from PyQt5.Qtwidgets import Qwidget
app= QApplication(sys.argv)
w= Qwidget()
w.setWindowTitle('Phone Book')
w.setGeometry(10, 100, 280, 80)
w.show()
app.exec_()



class ContactDialog(QDialog):
    def__init__(self, parent=None)
    super().__init__(parent)
    self.first_name_edit = QLineEdit()
    self.last_name_edit=QLineEdit()
    save_button=QPushButton(parent=self , text='save')
    save_button.clicked.connect(self.save_contact)
    form_layout = QFormLayout()
    form_layout.addRow('first name', self)
    form_layout.addRow('last name', self)
    form_layout.addRow('' , save_button)
    self.setLayout(form_layout)
    def save_contact(self):
        print(self.first_name_edit.text())
        print(self.last_name_edit.text())



