import sys
from PyQt6.QtWidgets import QApplication
from main_window import LogicAnalyzerWindow
import pyqtgraph as pg

def main():
    # Set dark theme for pyqtgraph
    pg.setConfigOption('background', '#121212')
    pg.setConfigOption('foreground', '#d3d3d3')
    
    app = QApplication(sys.argv)
    
    # Set global dark stylesheet for the application UI
    app.setStyleSheet("""
        QMainWindow, QWidget {
            background-color: #1e1e1e;
            color: #d3d3d3;
        }
        QPushButton {
            background-color: #333333;
            border: 1px solid #555555;
            padding: 5px 15px;
            color: #ffffff;
            border-radius: 3px;
        }
        QPushButton:hover {
            background-color: #505050;
        }
        QComboBox, QSpinBox {
            background-color: #2d2d2d;
            border: 1px solid #555555;
            padding: 3px;
            color: #ffffff;
        }
        QLabel {
            color: #d3d3d3;
        }
    """)
    
    window = LogicAnalyzerWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
