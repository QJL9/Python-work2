import sys
from PySide2 import QtGui
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QLabel
from PySide2.QtCore import QFile, QIODevice
if __name__ == "__main__":
    ui_file_name = "mainwindow.ui"
    app=QApplication([])

    ui_file = QFile("main.ui")
    if not ui_file.open(QIODevice.ReadOnly):
            print("Cannot open {}: {}".format(ui_file_name, ui_file.errorString()))
            sys.exit(-1)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()    
    if not window:
        print(loader.errorString())
        sys.exit(-1)
    movie=QtGui.QMovie(":/3891.gif")
    window.label.setMovie(movie)
   
    movie.start()
    window.show()



window.show()
sys.exit(app.exec_())