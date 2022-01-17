from PyQt5 import uic, QtWidgets

def somar():
    soma = 0
    if (primeira_tela.checkBox_2.isChecked()):
        soma += 20
    if (primeira_tela.checkBox_4.isChecked()):
        soma += 32
    if (primeira_tela.checkBox_3.isChecked()):
        soma += 10
    if (primeira_tela.checkBox.isChecked()):
        soma += 15
    if (primeira_tela.checkBox_5.isChecked()):
        soma += 5.5

    primeira_tela.label.setText("Valor total: "+str(soma))


app=QtWidgets.QApplication([])
primeira_tela=uic.loadUi("check_box.ui")
primeira_tela.pushButton.clicked.connect(somar)

primeira_tela.show()
app.exec()