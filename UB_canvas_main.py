#By Nery Ruiz

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog
from Sign_in import Ui_Dialog
from queue import Queue
import threading
#from Admin_Dialog import Ui_admin_window


class Main(QDialog):
    def __init__(self):
        self.q = Queue()
        self.q.put('None')
        app = QApplication(sys.argv)
        dia = QDialog()
        self.ui =Ui_Dialog()
        self.ui.setupUi(dia)
        dia.show()
        #t = threading.Thread(name='sign in', target=self.run)
        #t.start()
        sys.exit(app.exec_())
        print("done")
        #app.exec_()
        
    def run(self):
        '''while True:
            print('tes')
            print(self.q.get())
            if(self.q.get() != 'None'):
                break
            else:
                pass'''
        print(self.q.get())
        

main = Main()
