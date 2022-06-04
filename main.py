import sys
from pathlib import Path
from tkinter import Widget
from turtle import home
from PyQt6.QtWidgets import (
    QApplication, 
    QPushButton, 
    QHBoxLayout, 
    QVBoxLayout, 
    QGridLayout, 
    QMainWindow,
    QFileDialog,
    QLabel, 
    QWidget)

from PyQt6.QtGui import QPalette, QColor
from video_conv import Video



class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Fyv")
        self.setFixedSize(400, 300)

        widget = QWidget()
        

        layout = QGridLayout()
        widget.setLayout(layout)

        vid = QPushButton()
        vid.setFixedSize(150, 150)
        layout.addWidget(vid, 0, 0)
        vid.setText("Convert video formats")
        vid.pressed.connect(self.showDialog)

        vid1 = QPushButton()
        vid1.setFixedSize(150, 150)
        layout.addWidget(vid1, 0, 1)
        vid1.setText("Convert video to mp3")


        self.setCentralWidget(widget)

    def showDialog(self):

        self.next = Video()
        self.next.show()

        
   

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()