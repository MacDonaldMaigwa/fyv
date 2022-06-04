from subprocess import*
from pathlib import Path
from PyQt6.QtWidgets import (
    QWidget, 
    QPushButton, 
    QComboBox,
    QLabel,
    QHBoxLayout, 
    QVBoxLayout,
    QLineEdit,
    QProgressBar,
    QMainWindow,
    QFrame,
    QFileDialog,
    QApplication)
from PyQt6.QtCore import QRect

class Video(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Convert video")
        self.setFixedSize(300, 340)

        self.formarts = QComboBox()
        self.fpath = QLineEdit()
        self.browse = QPushButton()
        self.fmt_label = QLabel()
        self.flabel = QLabel()

        self.progress = QProgressBar()
        self.convert = QPushButton()

        
        self.formarts.addItems(["avi", "mp4", "ogg", "webm", "wmv", "mov", "flv"])
        self.convert.clicked.connect(self.Convert)

        self.browse.clicked.connect(self.selctFile)
        self.convert.setMaximumWidth(60)
        #self.formarts.setGeometry(QRect(10, 30, 20, 10))
        

        #self.flabel.setFixedHeight(10)
        #self.flabel.setFixedSize(20, 40)
        #self.flabel.setStyleSheet("background-color: red;")

        self.flabel.setText("Select video file")
        #self.flabel.setStyleSheet("margin-top: 100px")
       
        self.browse.setText("Browse")
        self.fmt_label.setText("Select format: ")
        self.convert.setText("Convert")
        self.progress.setValue(35)

        self.fframe = QFrame()
        self.fmt_frame = QFrame()
        self.cvt_frame = QFrame()
        self.fframe.setMaximumHeight(60)
        self.fmt_frame.setMaximumHeight(50)
        self.cvt_frame.setMaximumHeight(50)

    
        
        layout = QVBoxLayout()
        layout1 = QVBoxLayout()
        sel_layout = QHBoxLayout()
        fmt_layout = QHBoxLayout()
        cvt_layout = QHBoxLayout()


        layout.addWidget(self.fframe)
        layout.addWidget(self.fmt_frame)
        layout.addWidget(self.progress)
        layout.addWidget(self.cvt_frame)
        self.cvt_frame.setLayout(cvt_layout)
        cvt_layout.addWidget(self.convert)
        self.fframe.setLayout(layout1)
        self.fmt_frame.setLayout(fmt_layout)

        fmt_layout.addWidget(self.fmt_label)
        fmt_layout.addWidget(self.formarts)
        layout1.addWidget(self.flabel)
        layout1.addLayout(sel_layout)
        sel_layout.addWidget(self.fpath)
        sel_layout.addWidget(self.browse)

        self.setLayout(layout)

    def selctFile(self):
            #wel = "Welcome Here!"
        home_dir = str(Path.home())
        self.fname = QFileDialog.getOpenFileName(self, 'Open Video', home_dir)
        self.name = self.fname[0]

        self.fpath.setText(self.name)

    def Convert(self):
        file = "new"
        format = self.formarts.currentText()
        run("ffmpeg -i {} {}.{}".format(self.name, file, format))
        self.convert.setDisabled(True)