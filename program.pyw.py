import sys
from PyQt4 import  QtGui, QtCore
from converter import *


class programa(QtGui.QWidget):

    def __init__(self, parent=None):

        QtGui.QWidget.__init__(self,parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.error.setText("presure cnverter")
        #self.ui.entrada.textChanged()
        unidades = ['kiloPascal', 'Bar', 'Psi', 'centimeter of water','atmosphere','milimeters of mercury']
        for i in unidades:
            self.ui.comboBox.addItems([i])
            self.ui.comboBox_2.addItems([i])

        print(self.ui.comboBox.currentIndex()==0)

        if self.ui.comboBox.itemText(0) and self.ui.convertir.clicked.connect(self.converter_kilo_to):
            self.converter_kilo_to()

        elif self.ui.comboBox.itemText(1) and self.ui.convertir.clicked.connect(self.converter_Bar_to_):
            self.converter_Bar_to()

        elif self.ui.comboBox.itemText(2) and self.ui.convertir.clicked.connect(self.converter_psi_to_):
            self.converter_psi_to_()

        elif self.ui.comboBox.itemText(3) and self.ui.convertir.clicked.connect(self.converter_cmh2o_to_):
            self.converter_cmh2o_to_()

        elif self.ui.comboBox.itemText(4) and self.ui.convertir.clicked.connect(self.converter_atm_to_):
            self.converter_atm_to_()

        elif self.ui.comboBox.itemText(5) and self.ui.convertir.clicked.connect(self.converter_mmhg_to_):
            self.converter_mmhg_to_()





    def converter_kilo_to(self):



        try:
            a = float(self.ui.entrada.text())

            if self.ui.comboBox.currentIndex()==0 and self.ui.comboBox_2.currentIndex()==0:

                self.ui.salida.setText("{} {}".format(a, self.ui.comboBox_2.currentText()))

            elif self.ui.comboBox.itemText(0) and self.ui.comboBox_2.currentIndex()==1:

                self.ui.salida.setText("{} {}".format(a*0.01, self.ui.comboBox_2.currentText()))

            elif self.ui.comboBox.itemText(0) and self.ui.comboBox_2.currentIndex() == 2:

                self.ui.salida.setText("{:.5f} {}".format(a*0.15, self.ui.comboBox_2.currentText()))

            elif self.ui.comboBox.itemText(0) and self.ui.comboBox_2.currentIndex() == 3:

                self.ui.salida.setText("{:.5f} {}".format(a*10.2, self.ui.comboBox_2.currentText()))

            elif self.ui.comboBox.itemText(0) and self.ui.comboBox_2.currentIndex() == 4:

                self.ui.salida.setText("{:.5f} {}".format(a * 0.00986, self.ui.comboBox_2.currentText()))

            elif self.ui.comboBox.itemText(0) and self.ui.comboBox_2.currentIndex() == 5:

                self.ui.salida.setText("{:.5f} {}".format(a * 7.500, self.ui.comboBox_2.currentText()))

        except ValueError:
            self.ui.error.setText("please only numbers")


    def converter_Bar_to_(self):



        try:
            a = float(self.ui.entrada.text())

            if self.ui.comboBox.currentIndex() == 1 and self.ui.comboBox_2.currentIndex() == 0:

                self.ui.salida.setText("{} {}".format((a*1)/0.01, self.ui.comboBox_2.currentText()))


            elif self.ui.comboBox.currentIndex() == 1 and self.ui.comboBox_2.currentIndex() == 1:

                self.ui.salida.setText("{} {}".format((a * 1), self.ui.comboBox_2.currentText()))


            elif self.ui.comboBox.currentIndex() == 1 and self.ui.comboBox_2.currentIndex() == 2:

                self.ui.salida.setText("{} {}".format((a * 14.50), self.ui.comboBox_2.currentText()))

            elif self.ui.comboBox.currentIndex() == 1 and self.ui.comboBox_2.currentIndex() == 3:

                self.ui.salida.setText("{} {}".format((a * 1019.74), self.ui.comboBox_2.currentText()))

            elif self.ui.comboBox.currentIndex() == 1 and self.ui.comboBox_2.currentIndex() == 4:

                self.ui.salida.setText("{} {}".format((a * 0.9869), self.ui.comboBox_2.currentText()))

            elif self.ui.comboBox.currentIndex() == 1 and self.ui.comboBox_2.currentIndex() == 4:

                self.ui.salida.setText("{} {}".format((a * 0.9869), self.ui.comboBox_2.currentText()))

            elif self.ui.comboBox.currentIndex() == 1 and self.ui.comboBox_2.currentIndex() == 5:

                self.ui.salida.setText("{} {}".format((a *750.06 ), self.ui.comboBox_2.currentText()))



        except ValueError:
            self.ui.error.setText("please only numbers")

    def converter_psi_to_(self):


        try:
            a = float(self.ui.entrada.text())

            if self.ui.comboBox.currentIndex() == 2 and self.ui.comboBox_2.currentIndex() == 0:

                self.ui.salida.setText("{:.3f} {}".format((a*1)/0.1450, self.ui.comboBox_2.currentText()))

            if self.ui.comboBox.currentIndex() == 2 and self.ui.comboBox_2.currentIndex() == 1:

                self.ui.salida.setText("{:.3f} {}".format((a * 1) / 14.50, self.ui.comboBox_2.currentText()))

            if self.ui.comboBox.currentIndex() == 2 and self.ui.comboBox_2.currentIndex() == 2:

                self.ui.salida.setText("{:.3f} {}".format((a * 1), self.ui.comboBox_2.currentText()))

            if self.ui.comboBox.currentIndex() == 2 and self.ui.comboBox_2.currentIndex() == 3:

                self.ui.salida.setText("{:.3f} {}".format((a * 70.31), self.ui.comboBox_2.currentText()))

            if self.ui.comboBox.currentIndex() == 2 and self.ui.comboBox_2.currentIndex() == 4:

                self.ui.salida.setText("{:.3f} {}".format((a * 0.068046), self.ui.comboBox_2.currentText()))

            elif self.ui.comboBox.currentIndex() == 2 and self.ui.comboBox_2.currentIndex() ==5:

                self.ui.salida.setText("{:.3f} {}".format((a * 51.72), self.ui.comboBox_2.currentText()))




        except ValueError:
            self.ui.error.setText("please only numbers")



    def converter_cmh2o_to_(self):


        try:
            a = float(self.ui.entrada.text())
            if self.ui.comboBox.currentIndex() == 3 and self.ui.comboBox_2.currentIndex() == 0:

                self.ui.salida.setText("{:.3f} {}".format((a * 1)/10.2, self.ui.comboBox_2.currentText()))

            elif self.ui.comboBox.currentIndex() == 3 and self.ui.comboBox_2.currentIndex() == 1:

                self.ui.salida.setText("{:.3f} {}".format((a * 1) / 1019.74, self.ui.comboBox_2.currentText()))

            elif self.ui.comboBox.currentIndex() == 3 and self.ui.comboBox_2.currentIndex() == 2:

                self.ui.salida.setText("{:.3f} {}".format((a * 0.01) , self.ui.comboBox_2.currentText()))
                print('where Am i1')

            elif self.ui.comboBox.currentIndex() == 3 and self.ui.comboBox_2.currentIndex() == 3:

                self.ui.salida.setText("{:.3f} {}".format((a * 1), self.ui.comboBox_2.currentText()))

            elif self.ui.comboBox.currentIndex() == 3 and self.ui.comboBox_2.currentIndex() == 4:

                self.ui.salida.setText("{:.3f} {}".format((a * 1)/1033.26, self.ui.comboBox_2.currentText()))

            elif self.ui.comboBox.currentIndex() == 3 and self.ui.comboBox_2.currentIndex() == 5:

                self.ui.salida.setText("{:.3f} {}".format((a * 0.74) , self.ui.comboBox_2.currentText()))


        except ValueError:
            self.ui.error.setText("please only numbers")

    def converter_atm_to_(self):


        try:
            a = float(self.ui.entrada.text())
            if self.ui.comboBox.currentIndex() == 4 and self.ui.comboBox_2.currentIndex() == 0:

                self.ui.salida.setText("{:.3f} {}".format((a * 101.32), self.ui.comboBox_2.currentText()))

            elif self.ui.comboBox.currentIndex() == 4 and self.ui.comboBox_2.currentIndex() == 1:

                self.ui.salida.setText("{:.3f} {}".format((a * 1.01), self.ui.comboBox_2.currentText()))

            elif self.ui.comboBox.currentIndex() == 4 and self.ui.comboBox_2.currentIndex() == 2:

                self.ui.salida.setText("{:.3f} {}".format((a * 14.7), self.ui.comboBox_2.currentText()))

            elif self.ui.comboBox.currentIndex() == 4 and self.ui.comboBox_2.currentIndex() == 3:

                self.ui.salida.setText("{:.3f} {}".format((a * 1033.26), self.ui.comboBox_2.currentText()))

            elif self.ui.comboBox.currentIndex() == 4 and self.ui.comboBox_2.currentIndex() == 4:

                self.ui.salida.setText("{:.3f} {}".format((a * 1), self.ui.comboBox_2.currentText()))

            elif self.ui.comboBox.currentIndex() == 4 and self.ui.comboBox_2.currentIndex() == 5:

                self.ui.salida.setText("{:.3f} {}".format((a * 760), self.ui.comboBox_2.currentText()))



        except ValueError:
            self.ui.error.setText("please only numbers")

    def converter_mmhg_to_(self):

        try:

            a = float(self.ui.entrada.text())
            if self.ui.comboBox.currentIndex() == 5 and self.ui.comboBox_2.currentIndex() == 0:

                self.ui.salida.setText("{:.3f} {}".format((a * 0.13), self.ui.comboBox_2.currentText()))

            elif self.ui.comboBox.currentIndex() == 5 and self.ui.comboBox_2.currentIndex() == 1:

                self.ui.salida.setText("{:.5f} {}".format((a * 1)/750.6, self.ui.comboBox_2.currentText()))

            elif self.ui.comboBox.currentIndex() == 5 and self.ui.comboBox_2.currentIndex() == 2:

                self.ui.salida.setText("{:.5f} {}".format((a * 0.02), self.ui.comboBox_2.currentText()))

            elif self.ui.comboBox.currentIndex() == 5 and self.ui.comboBox_2.currentIndex() == 3:

                self.ui.salida.setText("{:.5f} {}".format((a * 1.36), self.ui.comboBox_2.currentText()))

            elif self.ui.comboBox.currentIndex() == 5 and self.ui.comboBox_2.currentIndex() == 4:

                self.ui.salida.setText("{:.5f} {}".format((a * 1)/760.0, self.ui.comboBox_2.currentText()))

            elif self.ui.comboBox.currentIndex() == 5 and self.ui.comboBox_2.currentIndex() == 5:

                self.ui.salida.setText("{:.5f} {}".format((a * 1), self.ui.comboBox_2.currentText()))

        except ValueError:
            self.ui.error.setText("please only numbers")










if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    mi_app = programa()
    mi_app.show()
    sys.exit(app.exec_())
