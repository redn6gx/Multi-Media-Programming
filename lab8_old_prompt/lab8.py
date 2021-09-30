# Bobby Davis
# IMPORTS

import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QDialog, QTextBrowser, QComboBox, QLineEdit
from PySide6.QtCore import Qt, Slot

#-----------------------------------------------------------------------------------------------

# TASK 1

# my_qt_app = QApplication([])

# class ColorWindow(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle('Background')
#         p = self.palette()
#         p.setColor(self.backgroundRole(), Qt.darkMagenta)
#         self.setPalette(p)

# my_window = ColorWindow()

# x = my_window.palette()
# x.setColor(my_window.backgroundRole(), Qt.darkCyan)
# my_window.setPalette(x)

# my_window.show()

# sys.exit(my_qt_app.exec_())

#-----------------------------------------------------------------------------------------------

#TASK 2

# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()

#         # 3 Verticle Columns
#         v_layout1 = QVBoxLayout()
#         h1 = QPushButton("A")
#         b1 = QPushButton("1")
#         b2 = QPushButton("4")
#         b3 = QPushButton("7")

#         v_layout1.addWidget(h1)
#         v_layout1.addWidget(b1)
#         v_layout1.addWidget(b2)
#         v_layout1.addWidget(b3)

#         v_layout2 = QVBoxLayout()
#         h2 = QPushButton("B")
#         b4 = QPushButton("2")
#         b5 = QPushButton("5")
#         b6 = QPushButton("8")

#         v_layout2.addWidget(h2)
#         v_layout2.addWidget(b4)
#         v_layout2.addWidget(b5)
#         v_layout2.addWidget(b6)

#         v_layout3 = QVBoxLayout()
#         h3 = QPushButton("C")
#         b7 = QPushButton("3")
#         b8 = QPushButton("6")
#         b9 = QPushButton("9")

#         v_layout3.addWidget(h3)
#         v_layout3.addWidget(b7)
#         v_layout3.addWidget(b8)
#         v_layout3.addWidget(b9)

#         # outer layer
#         main_layout = QHBoxLayout()

#         # add previous two inner layouts
#         # main_layout.addLayout(h_layout)
#         main_layout.addLayout(v_layout1)
#         main_layout.addLayout(v_layout2)
#         main_layout.addLayout(v_layout3)

#         # set outer layout as a main layout of the widget
#         self.setLayout(main_layout)

#         # window title
#         self.setWindowTitle("Layouts")

#         self.show()

# app = QApplication([])

# # create an instance of MyWindow
# w = MyWindow()

# sys.exit(app.exec_())

#-----------------------------------------------------------------------------------------------

# TASK 3

# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         vbox = QVBoxLayout()
#         self.my_btn1 = QPushButton("Button 1")
#         self.my_btn2 = QPushButton("Button 2")

#         self.my_lbl = QLabel('Button Not clicked')

#         self.my_btn1.clicked.connect(self.on_click1)
#         self.my_btn2.clicked.connect(self.on_click2)

#         vbox.addWidget(self.my_btn1)
#         vbox.addWidget(self.my_btn2)
#         vbox.addWidget(self.my_lbl)

#         self.setLayout(vbox)

#     @Slot()
#     def on_click1(self):
#         self.my_lbl.setText('Button 1 clicked')
#         self.repaint()
#     @Slot()    
#     def on_click2(self):
#         self.my_lbl.setText('Button 2 clicked')
#         self.repaint()

# app = QApplication([])
# my_win = MyWindow()
# my_win.show()
# app.exec_()

#-----------------------------------------------------------------------------------------------

# TASK 4

class ColorWindow(QWidget):
    def __init__(self, color):
        super().__init__()

        self.setWindowTitle('Background')
        p = self.palette()
        p.setColor(self.backgroundRole(), color)
        self.setPalette(p)

class MyWindow(QWidget):
  def __init__(self):
    super().__init__()

    self.my_list = ['red', 'green', 'blue', 'orange', 'purple', 'white', 'black', 'cyan', 'magenta']
    self.combo = QComboBox()
    self.combo.addItems(self.my_list)
    self.btn = QPushButton('CLICK ME')
    vbox = QVBoxLayout()
    vbox.addWidget(self.combo)
    vbox.addWidget(self.btn)
    self.setLayout(vbox)

    self.btn.clicked.connect(self.open_win)

  @Slot() 
  def open_win(self):
    i = self.combo.currentIndex()
    self.new_win = ColorWindow(self.my_list[i])
    self.new_win.show()
    self.repaint()

app = QApplication(sys.argv)
main = MyWindow()
main.show()
sys.exit(app.exec_())


