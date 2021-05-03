import ctypes
import numpy as np
import time
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
library = ctypes.CDLL('./libfft.so')

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(782, 460)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = PlotWidget(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(341, 271))
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_2, 0, 0, 1, 5)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget_2 = PlotWidget(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QtCore.QSize(341, 271))
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_2.addWidget(self.widget_2, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_3, 0, 5, 1, 2)
        self.DFT = QtWidgets.QPushButton(self.frame)
        self.DFT.setMaximumSize(QtCore.QSize(75, 23))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.DFT.setFont(font)
        self.DFT.setObjectName("DFT")
        self.gridLayout_3.addWidget(self.DFT, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(33, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 1, 1, 1)
        self.FFT = QtWidgets.QPushButton(self.frame)
        self.FFT.setMaximumSize(QtCore.QSize(75, 23))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.FFT.setFont(font)
        self.FFT.setObjectName("FFT")
        self.gridLayout_3.addWidget(self.FFT, 1, 2, 1, 1)
        self.clear = QtWidgets.QPushButton(self.frame)
        self.clear.setMaximumSize(QtCore.QSize(75, 23))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.clear.setFont(font)
        self.clear.setObjectName("clear")
        self.gridLayout_3.addWidget(self.clear, 1, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(7, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 1, 4, 1, 1)
        self.error = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.error.setFont(font)
        self.error.setObjectName("error")
        self.gridLayout_3.addWidget(self.error, 1, 5, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(246, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 1, 6, 1, 1)
        self.gridLayout_4.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 782, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.widgetsArray = [self.widget, self.widget_2]
        for i in range (2):
            self.widgetsArray[i].plotItem.addLegend(size=(1,2))
            self.widgetsArray[i].plotItem.setLabel('bottom', "Number of samples")
            self.widgetsArray[i].plotItem.showGrid(True, True, alpha = 0.5)
        
        self.widget_2.setYRange(-2, 2)
        self.widget.plotItem.setLabel('left', "Computation time", units = "s")
        self.widget_2.plotItem.setLabel('left', "Error")
        # doublesArray === double [4];
        # arr2 = doublesArray.from_address(np_array) ---- arr2 is double arr[4] in C
        self.N = np.array([1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024], dtype=np.int)
        self.i_real = np.arange((1024), dtype=np.double)
        self.i_imag = np.arange((1024), dtype=np.double)
        self.DFT.clicked.connect(lambda: self.plotting(index = 1))
        self.FFT.clicked.connect(lambda: self.plotting(index = 2))
        self.clear.clicked.connect(lambda: self.plotting(index = 3))
        self.error.clicked.connect(lambda: self.plotting(index = 4))
        self.dftTime = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype= np.double)
        self.fftTime = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype= np.double)
        self.i_size = len(self.i_real)
        doublesArray = ctypes.c_double * self.i_size
        i_real_C = doublesArray.from_address(self.i_real.ctypes.data)
        i_imag_C = doublesArray.from_address(self.i_imag.ctypes.data)

        o_real_ptr = ctypes.POINTER(ctypes.c_double)()
        o_imag_ptr = ctypes.POINTER(ctypes.c_double)()
        o_size = ctypes.c_int()

        library.C_fft(i_real_C, i_imag_C, self.i_size, ctypes.byref(o_real_ptr), ctypes.byref(o_imag_ptr), ctypes.byref(o_size))


        fft_o_real = o_real_ptr[:o_size.value]
        fft_o_imag = o_imag_ptr[:o_size.value]

        

        library.C_dft(i_real_C, i_imag_C, self.i_size, ctypes.byref(o_real_ptr), ctypes.byref(o_imag_ptr), ctypes.byref(o_size))
        
        dft_o_real = o_real_ptr[:o_size.value]
        dft_o_imag = o_imag_ptr[:o_size.value]

        error_real =  np.subtract(dft_o_real ,fft_o_real)
        error_imag =  np.subtract(dft_o_imag ,fft_o_imag)
        error = np.multiply(error_real, error_imag)
        self.errorArray = error[0: 11]

        print("error :",self.errorArray)
# g++ -fPIC -shared -o libfft.so fft.cpp && python run.py


    def plotting(self, index):
        global i_size
        global i_real_C
        size = len(self.N)
        for i in range (size):
            start_time = time.time()
            self.i_real_iteration = self.i_real[0: self.N[i]]
            self.i_imag_iteration = self.i_imag[0: self.N[i]]
            i_size = len(self.i_real_iteration)
            doublesArray = ctypes.c_double * self.N[i]
            i_real_C = doublesArray.from_address(self.i_real_iteration.ctypes.data)
            i_imag_C = doublesArray.from_address(self.i_imag_iteration.ctypes.data)
            o_real_ptr = ctypes.POINTER(ctypes.c_double)()
            o_imag_ptr = ctypes.POINTER(ctypes.c_double)()
            o_size = ctypes.c_int()
            if ( index == 1):
                library.C_dft(i_real_C, i_imag_C, i_size, ctypes.byref(o_real_ptr), ctypes.byref(o_imag_ptr), ctypes.byref(o_size))
                self.dftTime[i] = (time.time() - start_time)
            if (index == 2):
                library.C_fft(i_real_C, i_imag_C, i_size, ctypes.byref(o_real_ptr), ctypes.byref(o_imag_ptr), ctypes.byref(o_size))
                print(i_size)
                self.fftTime[i] = (time.time() - start_time)
            if (index == 3):
                self.widget.clear()
                self.widget_2.clear()
        if (index == 1):
            print(self.dftTime)
            self.widget.plot(self.N, self.dftTime, name = "DFT", pen = "r")
        if (index == 2):
            print(self.fftTime)
            self.widget.plot(self.N, self.fftTime, name = "FFT", pen = "b")
        if (index == 4):
            self.widget_2.plot(self.N, self.errorArray, name = "Error", pen = "r")
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DFT vs FFT"))
        self.DFT.setText(_translate("MainWindow", "Draw DFT"))
        self.DFT.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.FFT.setText(_translate("MainWindow", "Draw FFT"))
        self.FFT.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.clear.setText(_translate("MainWindow", "Clear"))
        self.clear.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.error.setText(_translate("MainWindow", "Show Error"))
        self.error.setShortcut(_translate("MainWindow", "Ctrl+E"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



