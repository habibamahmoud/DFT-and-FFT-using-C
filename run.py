import ctypes
import numpy as np
import time
import sys
from task3 import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton
library = ctypes.CDLL('./libfft.so')

class Functions (Ui_MainWindow):
    def __init__(self, window):
        doublesArray = ctypes.c_double * 4

        # doublesArray === double [4];
        # arr2 = doublesArray.from_address(np_array) ---- arr2 is double arr[4] in C
        N = np.array([1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024], dtype=np.double)
        i_real = np.arange((1024), dtype=np.double)
        i_imag = np.arange((1024), dtype=np.double)
        self.DFT.clicked.connect(self.plotting(self, 1))
        self.FFT.clicked.connect(self.plotting(self, 2))
        """ i_size = len(i_real)
        i_real_C = doublesArray.from_address(i_real.ctypes.data)
        i_imag_C = doublesArray.from_address(i_imag.ctypes.data)

        o_real_ptr = ctypes.POINTER(ctypes.c_double)()
        o_imag_ptr = ctypes.POINTER(ctypes.c_double)()
        o_size = ctypes.c_int()

        library.C_fft(i_real_C, i_imag_C, i_size, ctypes.byref(o_real_ptr), ctypes.byref(o_imag_ptr), ctypes.byref(o_size))


        o_real = o_real_ptr[:o_size.value]
        o_imag = o_imag_ptr[:o_size.value]

        print(o_real)
        print(o_imag) """
# g++ -fPIC -shared -o libfft.so fft.cpp && python run.py

    def plotting(self, index):
        size = len(N)
        for i in range (size):
            if ( index == 1):
                start_time = time.time()
                i_real = i_real[0: N[i]-1]
                i_imag = i_imag[0: N[i]-1]
                i_size = len(i_real)
                i_real_C = doublesArray.from_address(i_real.ctypes.data)
                i_imag_C = doublesArray.from_address(i_imag.ctypes.data)
                o_real_ptr = ctypes.POINTER(ctypes.c_double)()
                o_imag_ptr = ctypes.POINTER(ctypes.c_double)()
                o_size = ctypes.c_int()
                library.C_dft(i_real_C, i_imag_C, i_size, ctypes.byref(o_real_ptr), ctypes.byref(o_imag_ptr), ctypes.byref(o_size))
                self.dftTime[i] = (time.time() - start_time)
            if (index == 2):
                start_time = time.time()
                i_real = i_real[0: N[i]-1]
                i_imag = i_imag[0: N[i]-1]
                i_size = len(i_real)
                i_real_C = doublesArray.from_address(i_real.ctypes.data)
                i_imag_C = doublesArray.from_address(i_imag.ctypes.data)
                o_real_ptr = ctypes.POINTER(ctypes.c_double)()
                o_imag_ptr = ctypes.POINTER(ctypes.c_double)()
                o_size = ctypes.c_int()
                library.C_fft(i_real_C, i_imag_C, i_size, ctypes.byref(o_real_ptr), ctypes.byref(o_imag_ptr), ctypes.byref(o_size))
                self.fftTime[i] = (time.time() - start_time)
        if (index == 1):
            self.widget.plot(self.N, self.dftTime, name = "DFT", pen = "r")
        if (index == 2):
            self.widget.plot(self.N, self.fftTime, name = "FFT", pen = "b")
        self.widget.plotItem.addLegend(size=(1,2))
        self.widget.plotItem.showGrid(True, True, alpha = 0.5)
        self.widget.plotItem.setLabel('bottom', "Number of samples")
        self.widget.plotItem.setLabel('left', "Computation time", units = "s")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())