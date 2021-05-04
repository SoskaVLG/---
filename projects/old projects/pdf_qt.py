import easygui as g 
import win32com.client
from PIL import Image
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet("background {\n"
"rgb(223, 238, 237)}")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 220, 91, 71))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(image2pdf )
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 220, 101, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(word2pdf)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, -20, 331, 111))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "PyPDFConverter"))
        self.pushButton.setText(_translate("Dialog", "Изображения"))
        self.pushButton_2.setText(_translate("Dialog", "Word"))
        self.label.setText(_translate("Dialog", "Выберите тип файлов"))

def word2pdf (self) :
    try :
        wdFormatPDF = 17

        word = win32com.client.Dispatch('Word.Application')
        indirec = g.fileopenbox ("Выберите файл .docx")
        
        doc = word.Documents.Open(indirec)
        
        outdirec = g.filesavebox ("Выберите место для сохранения")
        doc.SaveAs(outdirec + ".pdf", FileFormat=wdFormatPDF)
        doc.Close()
        word.Quit()
        Dialog.show()
    except : 
        Dialog.show()
    return 0 

def image2pdf () :
    try :
        num = g.enterbox (title = "Количество изображений " , msg = "Введите количество изображений которые хотите добавить ")
        n = int (num)

        indir = g.fileopenbox ("Выберите изображение в формате JPEG или PNG")
        image1 = Image.open(str(indir))
        im1 = image1.convert ('RGB')
        n -= 1
        imagelist = []

        while n!=0 :
            indir_1 = g.fileopenbox ("Выберите изображение в формате JPEG или PNG")
            image2 = Image.open(str(indir_1))
            im2 = image2.convert ('RGB')
            imagelist.append (im2)
            n -= 1
        todir = g.filesavebox("Выберите место для сохранения")
        im1.save(str(todir) + ".pdf" , save_all= True , append_images=imagelist)
        Dialog.show()
    except:
        Dialog.show()
    return 0 




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())